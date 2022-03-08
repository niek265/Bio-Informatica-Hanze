#!/usr/bin/env python3

"""
Acceses a database and retrieves exam information from it.
"""

__version__ = '1.0'
__author__ = 'Niek Scholten'
__status__ = 'Finished'

import sys
import argparse
import getpass
import mysql.connector
from opdracht_1 import Tentamen


class Password:
    """
    Prompts the user for a password for secure input.
    """
    DEFAULT = ''

    def __init__(self, value):
        """
        Creates a password prompt.
        :param value: The value of the default password.
        """
        if value == self.DEFAULT:
            # Creates a prompt if the password is not yet defined
            value = getpass.getpass('Wachtwoord: ')
        self.value = value

    def __str__(self):
        """
        Sends the password to argparse.
        :return: Password.
        """
        return self.value


class DConnect:
    """
    Connects to the database and retrieves the desired information.
    """
    def __init__(self, username, password, host, database, name=None):
        """
        Assigns the variables.
        :param username: Database username.
        :param password: Database password.
        :param host: Database host.
        :param database: Database name.
        :param name: Name to look up in the database.
        """
        self.username = username
        self.password = str(password)
        self.host = host
        self.database = database
        self.argname = name
        self.cnx = mysql.connector.connect(user=self.username, password=self.password,
                                           host=self.host,
                                           database=self.database)
        self.names = []
        self.objects = []

    def get_names(self):
        """
        Retrieves the student names from the database.
        :return: Student names.
        """
        # Set a cursor
        cursor = self.cnx.cursor()
        query = "SELECT naam FROM studenten"
        cursor.execute(query)
        # Retrieve the contents from the query
        contents = cursor.fetchall()
        for name in contents:
            # Append the strings to a list
            self.names.append(name[0])
        return self.names

    def get_results(self):
        """
        Retrieves the exam information for a specific student
        :return: List of exam objects.
        """
        # Define a query for the database
        query = f"SELECT cursussen.naam, examens.ex_datum, examens.cijfer FROM cursussen " \
                f"JOIN examens ON cursussen.cur_id = examens.cur_id " \
                f"JOIN studenten ON examens.stud_id = studenten.stud_id " \
                f"WHERE studenten.naam = \"{self.argname}\""
        cursor = self.cnx.cursor()
        # Execute the query
        cursor.execute(query)
        # Retrieve items from the query
        for item in cursor.fetchall():
            self.objects.append(Tentamen(self.argname,
                                         item[0],
                                         item[1].strftime("%d %B %Y"),  # Convert date-time object to a string
                                         item[2]))
        for entry in self.objects:
            print(entry)
        return self.objects


def parse_args():
    """
    Uses argparse to fetch the user given arguments.
    :return: A namespace with the user arguments.
    """
    parser = argparse.ArgumentParser(description="""
    Returns the names of the students in the database,
    if a student name is defined, the corresponding exams will be printed.
    Usage:
    python opdracht_2_3.py -u username -s host -d database [-s host -n name -p password]
    If no password argument is given, a prompt will appear that securely asks fot the password.
    If a name is given, the exam information will be printed.
    The standard host is "mariadb.bin" if you wish to use another, use -s.
    """)

    parser.add_argument("-u", "--username", type=str, help="Gebruikersnaam")
    parser.add_argument("-p", "--password", type=Password, help="Wachtwoord", default=Password.DEFAULT)
    parser.add_argument("-s", "--host", type=str, help="Database host", default='mariadb.bin')
    parser.add_argument("-d", "--database", type=str, help="Database naam")
    parser.add_argument("-n", "--name", type=str, help="Student naam")

    return parser.parse_args()


def main(args):
    """
    Main function for handling the objects.
    :param args: Arguments.
    :return: Exitcode.
    """
    # Initiate the connection
    connection = DConnect(args.username, args.password, args.host, args.database, args.name)
    print(connection.get_names())
    if args.name:
        connection.get_results()
    return 0


if __name__ == "__main__":
    EXITCODE = main(parse_args())
    sys.exit(EXITCODE)
