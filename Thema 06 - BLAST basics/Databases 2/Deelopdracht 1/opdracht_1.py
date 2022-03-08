#!/usr/bin/env python3

"""
Prints the contents of a object.
"""

__version__ = '1.0'
__author__ = 'Niek Scholten'
__status__ = 'Finished'

import sys
import argparse


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


def parse_args():
    """
    Uses argparse to fetch the user given arguments.
    :return: A namespace with the user arguments.
    """
    parser = argparse.ArgumentParser(description="""
    Returns the given variables in a formatted manner.
    Usage:
    python -s student -v vak -d datum -c cijfer
    """)
    # Adds the given arguments to the parser
    parser.add_argument("-s", "--student", type=str, help="Student naam")
    parser.add_argument("-v", "--vak", type=str, help="Vak van het tentamen")
    parser.add_argument("-d", "--datum", type=str, help="Tentamen datum")
    parser.add_argument("-c", "--cijfer", type=str, help="Behaald cijfer")

    return parser.parse_args()


def main(args):
    """
    Main function for handling the arguments.
    :param args: Arguments given.
    :return: Exitcode.
    """
    entry = Tentamen(args.student, args.vak, args.datum, args.cijfer)
    # Prints the contents from the object
    print(entry)
    return 0


if __name__ == "__main__":
    EXITCODE = main(parse_args())
    sys.exit(EXITCODE)
