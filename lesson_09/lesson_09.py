import unittest

from functions_lesson_09 import computer_price, find_substring, sum_two_numbers, sum_doubles_only, list_string

class MyTest(unittest.TestCase):

    def test_computer_price_positive(self):
        years = 1.5
        payment_per_month = 1179
        expected_result = 21222
        self.assertEqual(computer_price(years, payment_per_month), expected_result)

    def test_computer_price_negative(self):
        years = None
        payment_per_month = 1179
        with self.assertRaises(TypeError):
            computer_price(years, payment_per_month)

    def test_find_substring_positive(self):
        string_1 = "Hello, world!"
        string_2 = "world"
        expected_result = 7
        self.assertEqual(find_substring(string_1, string_2), expected_result)

    def test_find_substring_negative(self):
        string_1 = "The quick brown fox jumps over the lazy dog"
        string_2 = "cat"
        expected_result = -1
        self.assertEqual(find_substring(string_1, string_2), expected_result)

    def test_sum_two_numbers_positive(self):
        numb_1 = 10
        numb_2 = 12
        expected_result = 22
        self.assertEqual(sum_two_numbers(numb_1, numb_2), expected_result)

    def test_sum_two_numbers_negative(self):
        numb_1 = 10
        numb_2 = "Sasha"
        expected_result = None
        self.assertEqual(sum_two_numbers(numb_1, numb_2), expected_result)

    def test_sum_doubles_only_positive(self):
        my_list = [0, 1, 2, 2, 1, 10, 5, 6, 2, 4, 5, 10]
        expected_result = 32
        self.assertEqual(sum_doubles_only(my_list), expected_result)

    def test_sum_doubles_only_negative(self):
        my_list = "Sasha"
        with self.assertRaises(ValueError):
            sum_doubles_only(my_list)

    def test_list_string_positive(self):
        lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        self.assertEqual(list_string(lst1), expected_result)

    def test_list_string_negative(self):
        lst1 = None
        with self.assertRaises(TypeError):
            list_string(lst1)