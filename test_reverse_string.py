import unittest

from reverse_string import reverse_string


class ReverseStringTests(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_spaces_and_punctuation(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")

    def test_none_raises_exception(self):
        with self.assertRaises(TypeError):
            reverse_string(None)


if __name__ == "__main__":
    unittest.main()
