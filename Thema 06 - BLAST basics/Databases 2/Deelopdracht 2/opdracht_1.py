#!/usr/bin/env python3

"""
Prints the contents of a database, or student info if asked for it.
"""

__version__ = '1.0'
__author__ = 'Niek Scholten'
__status__ = 'Finished'

import sys
import argparse
import mysql.connector


class Tentamen:
    """
    Stores student info.
    """
    def __init__(self, student, vak, datum, cijfer):
        """
        Stores all the info provided by the user.
        :param student: Student name.
        :param vak: Course.
        :param datum: Date of exam.
        :param cijfer: Grade.
        """
        self.student = student
        self.vak = vak
        self.datum = datum
        self.cijfer = cijfer

    def __str__(self):
        """
        Returns formatted student info.
        :return: A string containing the info from the object.
        """
        # Return a formatted string containing the requested info
        return (f"Student:\t{self.student}\n"
                f"Vak:\t{self.vak}\n"
                f"Datum:\t{self.datum}\n"
                f"Cijfer:\t{self.cijfer}\n")


class DConnect:
    """
    Connects to the database and retrieves the desired information.
    """
    def __init__(self, username=None, password=None, host=None, database=None, name=None, cnf=None):
        """
        Assigns the variables.
        :param username: Database username.
        :param password: Database password.
        :param host: Database host.
        :param database: Database name.
        :param name: Name to look up in the database.
        :param cnf: Config file.
        """
        self.username = username
        self.password = str(password)
        self.host = host
        self.database = database
        self.argname = name
        if username:  # If a username is given, connect using credentials
            self.cnx = mysql.connector.connect(user=self.username, password=self.password,
                                               host=self.host,
                                               database=self.database)
        else:  # If not, use the cnf file
            self.cnx = mysql.connector.connect(option_files=cnf)

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
        query = "SELECT cursussen.naam, examens.ex_datum, examens.cijfer FROM cursussen " \
                "JOIN examens ON cursussen.cur_id = examens.cur_id " \
                "JOIN studenten ON examens.stud_id = studenten.stud_id " \
                "WHERE studenten.naam = %s"
        cursor = self.cnx.cursor()
        # Execute the query
        cursor.execute(query, (self.argname,))
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
    python opdracht_1.py [-u username -s host -d database -s host -n name -p password -c config_file]
    If a name is given, the exam information will be printed.
    The standard .cnf file is my.cnf, if this is different, use -c.
    """)

    parser.add_argument("-u", "--username", type=str, help="Gebruikersnaam", default=None)
    parser.add_argument("-p", "--password", type=str, help="Wachtwoord", default=None)
    parser.add_argument("-s", "--host", type=str, help="Database host", default=None)
    parser.add_argument("-d", "--database", type=str, help="Database naam", default=None)
    parser.add_argument("-n", "--name", type=str, help="Student naam", default=None)
    parser.add_argument("-c", "--config", type=str, help="Config file", default='my.cnf')

    return parser.parse_args()


def main(args):
    """
    Main function for handling the objects.
    :param args: Arguments.
    :return: Exitcode.
    """
    # Initiate the connection
    connection = DConnect(args.username, args.password, args.host, args.database, args.name, args.config)
    print(connection.get_names())
    if args.name:
        connection.get_results()
    return 0


if __name__ == "__main__":
    EXITCODE = main(parse_args())
    sys.exit(EXITCODE)
