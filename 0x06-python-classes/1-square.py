#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """Instantiation with size: private attribute with no value"""
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
