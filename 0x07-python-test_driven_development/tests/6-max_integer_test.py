#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def setUp(self):
        """Set up the common test data before each test method."""
        self.test_cases = {
            'normal_case': [1, 2, 3, 4, 5],
            'empty_list': [],
            'negative_numbers': [-1, -2, -3, -4, -5],
            'single_element': [5],
            'mixed_numbers': [3, -1, 4, 0, -2],
            'floats': [1.1, 2.2, 3.3, 4.4],
            'strings': ["apple", "banana", "cherry"], }
        
    def tearDown(self):
        """Clean up after each test method."""
        self.test_cases.clear()

    def test_normal_cases(self):
        """Test with normal positive numbers"""
        self.assertEqual(max_integer(self.test_cases['normal_case']), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer(self.test_cases['empty_list']), None)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer(self.test_cases['negative_numbers']), -1)

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer(self.test_cases['single_element']), 5)

    def test_mixed_numbers(self):
        """Test with a mix of positive, negative, and zero"""
        self.assertEqual(max_integer(self.test_cases['mixed_numbers']), 4)

    def test_floats(self):
        """Test with float values"""
        self.assertEqual(max_integer(self.test_cases['floats']), 4.4)

    def test_strings(self):
        """Test with strings"""
        self.assertEqual(max_integer(self.test_cases['strings']), "cherry")

if __name__ == "__main__":
    unittest.main()
