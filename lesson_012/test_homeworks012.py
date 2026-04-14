
import unittest
from lesson_07.homework_07 import sum_num
from lesson_07.homework_07 import even_numbers
from lesson_07.homework_07 import count_title_words
from lesson_07.homework_07 import find_substring
from lesson_07.homework_07 import longest_word
from lesson_07.homework_07 import average
from lesson_07.homework_07 import reverse_string


class TestSumNumbers(unittest.TestCase):

    def test_sum_numbers_is_correct(self):
        result = sum_num(7, 8)
        self.assertEqual(result, 15)

        result = sum_num(-1, 1)
        self.assertEqual(result, 0)

    def test_even_numbers_list(self):
        result = even_numbers([6, 8, 1])
        self.assertEqual(result, [6, 8])


    def test_no_even_numbers(self):
        self.assertEqual(even_numbers([1, 3, 5]), [])

    def test_count_title_words(self):
        result = count_title_words("Tom Sawyer Is A Famous Book")
        self.assertEqual(result, 6)

    def test_find_substring(self):
        result = find_substring("Hello, world!", "world")
        self.assertEqual(result, 7)

    def test_find_substring_not_found(self):
        result = find_substring("The quick brown fox", "cat")
        self.assertEqual(result, -1)

    def test_longest_word(self):
        result = longest_word(['animals', 'flowers', 'hobby', 'book'])
        self.assertEqual(result, 'animals')
    def test_longest_word_not_found(self):
        result = longest_word(['animals', 'flowers', 'hobby', 'book'])
        self.assertNotEqual(result, 'hobby')

    def test_average(self):
        result = average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)
    def test_reverse_string(self):
        result = reverse_string("Hello")
        self.assertEqual(result, "olleH")


if __name__ == '__main__':
    unittest.main()
