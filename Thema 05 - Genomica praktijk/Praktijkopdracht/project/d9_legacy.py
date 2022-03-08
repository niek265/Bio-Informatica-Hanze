#!/usr/bin/env python3

"""
Gets a Annovar file and converts the data of some columns of interest
to a my.sql database consisting of a chromosome, genes and variants
table.

Usage: d9.py -n [database name] -u [database username] -p [password]
-f [filename] -s [host name]

This script is designed to run on python versions 3.6 and lower.
"""

import argparse
import sys
import re
from operator import itemgetter
import mysql.connector

__author__ = 'Niek Scholten, Rienk Heins'
__version__ = '1.1.0'
__email__ = 'n.r.scholten@st.hanze.nl, r.d.heins@st.hanze.nl'
__status__ = 'Finished'


class Annovar:
    """
    Annovar class object with functions to insert the data into a
    database
    filename: name of the file
    user: database username of the user
    name: name of the database
    password: password of the user
    """
    def __init__(self, arguments):
        self.file = arguments.file
        self.cnx = db_connect(arguments.name, arguments.username, arguments.password, arguments.host)
        self.chr_dict = {}
        self.gene_dict = {}

    def open_file(self):
        """
        Opens and reads through the file, it finds and uses the header
        to create dictionary's per line with the information to put
        into the database. Then it uses dictionary's to create unique
        id's for every chromosome, gene and variant. Then it uses
        the insert_table function to insert the data into the database.
        It also uses the function get_gene_name to change the RefSeq
        gene names into the correct names.
        :return: 0
        """
        columns = [0, 3, 4, 6, 10, 15, 16, 27, 33, 34, 35, 53]
        # a list with the desired columns with data
        chr_count = 0
        gene_count = 0
        variant_count = 0
        # creates counts to give id's to the data
        header_check = True
        # a check for the header
        print(F"Processing data from {self.file}...")
        filename = open(self.file)
        for line in filename:
            if not header_check:
                content = line.split("\t")
                data = itemgetter(*columns)(content)
                # uses itemgetter to create a tuple with the contents
                variant = dict(zip(header, data))
                # creates a dictionary with header table names as the
                # key and line data content as the value
                variant["RefSeq_Gene"] = get_gene_name(variant["RefSeq_Gene"])
                # uses get_gene_name to change the gene name into the
                # correct name
                if variant["chromosome"] not in self.chr_dict:
                    # checks if the chromosome is already in the data
                    # base by keeping track in a dictionary
                    chr_count += 1
                    # updates the chromosome id's
                    self.chr_dict[variant["chromosome"]] = chr_count
                    variant["chromosome_id"] = self.chr_dict[variant["chromosome"]]
                    # adds the chromosome id to the dict with the use of the chr_dict
                    self.insert_table("chromosomes", variant)
                    # inserts the data into the chromosomes table
                variant["chromosome_id"] = self.chr_dict[variant["chromosome"]]
                # gives id if the variant still has the same chromosome
                if variant["RefSeq_Gene"] not in self.gene_dict:
                    # checks it the gene is already in the database using gene_dict
                    gene_count += 1
                    # updates id
                    self.gene_dict[variant["RefSeq_Gene"]] = gene_count
                    variant["gene_id"] = self.gene_dict[variant["RefSeq_Gene"]]
                    # adds gene id to dict of the variant using gene_dict
                    self.insert_table("genes", variant)
                    # inserts the data into the genes table
                variant["gene_id"] = self.gene_dict[variant["RefSeq_Gene"]]
                # gives id if the variant is on the same gene
                variant_count += 1
                # updates variant id
                variant["variant_id"] = variant_count
                # adds variant id to the variant data
                self.insert_table("variants", variant)
                # inserts the data into the variants table
            else:
                # creates the header
                content = line.split("\t")
                header = itemgetter(*columns)(content)
                # uses itemgetter to create a tuple with the contents
                header_check = False
        self.cnx.commit()
        print("Committing data to database columns...")
        self.cnx.close()
        filename.close()
        # commits the data to the database and closes the connection object
        return 0

    def insert_table(self, table, variant):
        """
        Inserts the data of the Annovar file into the mysql database
        with the use of the mysql.connector import
        :param table: database table name
        :param variant: dictionary with variant data
        :return: 0
        """
        cursor = self.cnx.cursor()
        # creates a cursor
        cursor.execute("desc %s" % table)
        tdescription = cursor.fetchall()
        # gets the data of the table
        tcolumns = [column[0] for column in tdescription]
        # makes a list of all the column names in the table
        dcolumns = [column for column in tcolumns if column in variant]
        # gets the keys of the dictionary that match the column names

        query = "INSERT INTO {} ({}) VALUES ({})".format(table,
                                                         # List the column names
                                                         ', '.join(dcolumns),
                                                         # Format the VALUES as '(%(name)s, %(chr_id)s)'
                                                         ', '.join(['%({})s'.format(k) for k in dcolumns]))

        # creates a query for the sql database
        cursor.execute(query, variant)
        return 0


def db_connect(name, user, password, host):
    """
    Creates a database connection object that is used to connect
    to database and inserting of data
    :param name: Name of the database
    :param user: Username of the user
    :param password: Password of the user
    :param host: Host of the database
    :return: cnx connection object
    """
    cnx = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=name)
    # creates a database connection object

    return cnx


def get_gene_name(gene_name):
    """
    Gets a gene name and converts it into a correct name without
    the distance, LOC, LIN and NONE using regular expressions. If
    the name doesn't consists of correct gene names it will return
    -
    :param gene_name: name of a gene
    :return: correct gene name or - if no correct name is possible
    """
    gene = []
    # makes gene a list so it can be joined with a /, the desired
    # character if there are 2 or more names
    pattern = re.compile(r'[A-Z0-9]{3,}')
    matches = pattern.findall(gene_name)
    # matches everything with capital or digits
    for match in matches:
        if match.startswith(("NONE",
                             "LOC",
                             "LIN")) or re.match(r'\d', match):
            # passes on matches that are NONE, starting with LOC
            # or LIN or are digits only(distance value)
            pass
        else:
            gene.append(match)
    if not gene:
        gene = "-"
        # returns '-' if there are no appended values
    else:
        gene = "/".join(gene)
    return gene


def arg_parser():
    """
    Uses the argparse import to get information from the user from
    the command line and offers a user friendly help command
    :return: A namespace with the user arguments
    """
    parser = argparse.ArgumentParser(description="""
    Gets the database name, the username of the user, the password of
    the user, the server host name and the Annovar file for the 
    database to convert the Annovar data into a database for the user
    with the tables Chromosomes, Genes and Variants
    """)
    parser.add_argument("-n", "--name", type=str, help="Database name")
    parser.add_argument("-s", "--host", type=str, help="Database server host")
    parser.add_argument("-u", "--username", type=str, help="Database username of the user")
    parser.add_argument("-p", "--password", type=str, help="Password of the user")
    parser.add_argument("-f", "--file", type=str, help="Annovar file name")
    # uses argparse to get the user information for the database

    return parser.parse_args()


def main():
    """
    runs arg_paser() for user arguments and puts these arugments
    to run the Annovar class object
    :return: print statement informing the user the task is
    completed.
    """
    run = Annovar(arg_parser())
    run.open_file()
    return print("Program done!")


if __name__ == "__main__":
    sys.exit(main())
