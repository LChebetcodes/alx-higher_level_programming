#!/usr/bin/python3
"""
A Class MyList that inherits from list.
"""


class MyList(list):
    """A public instance method that prints the list"""
    def print_sorted(self):
        print(sorted(self))
