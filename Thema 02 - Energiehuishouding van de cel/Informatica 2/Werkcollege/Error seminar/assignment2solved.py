#!/usr/bin/env python3
#1 Toevoegen van een "
"""
A
silly
program
with a collection of syntax errors
"""

__author__ = "Tsjerk A. Wassenaar" #2 = toevoegen


# IMPORTS
import sys #3 : verwijderen


# CONSTANTS
times_pi = 6.283185 #4 2 verwijderen
mass = {
    "H": 1.008, #5 ; vervangen door ,
    "C": 12.011,
    "O": 15.998,
    } #6 } verwijderen


# FUNCTIONS
#7 def verwijderen

def fun(a, b, c): #8 : toegevoegd
    return a + (b * c) #9 haakjes weghalen


# MAIN
def main(args):
    print(fun(mass['H'], mass['C'], mass['O']))
    return 0


if __name__ == "__main__": #10 = toevoegen
    exitcode = main(sys.argv) #11 . verwijderen
    sys.exit(exitcode) #12 return exitcode vervangen
