#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Instantiation with size: private attribute with no value"""
    def __init__(self, size="0"):
        self.size = size

        @property
        def size(self):
            print("Retreiving size")

            return self.__size
