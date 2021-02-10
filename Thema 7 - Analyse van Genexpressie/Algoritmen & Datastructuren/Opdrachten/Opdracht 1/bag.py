#!/usr/bin/env

"""
Exercise 1.
"""

from random import randint

__author__ = "Niek Scholten"
__version__ = "1.0"


class Bag:
    """
    Contains a list and some operations for that list.
    """
    def __init__(self):
        """
        Creates the list.
        """
        self.items = []

    def add_item(self, item):
        """
        Adds an item to the list.
        """
        self.items.append(item)

    def get_item(self):
        """
        Retrieves a random item from the list.
        """
        return self.items[randint(0, len(self.items))]

    def remove_item(self, item):
        """
        Deletes an item from the list.
        """
        self.items.remove(item)
