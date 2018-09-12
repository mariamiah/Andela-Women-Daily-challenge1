from dictionary import returnDict, numbers
import unittest


class TestDict(unittest.TestCase):
    def test_return_dict(self):
        self.assertEqual(len(numbers), 15)
    
    def test_keys(self):
        self.assertEqual(numbers[1], 1)
        self.assertEqual(numbers[2], 4)
        self.assertEqual(numbers[5], 25)

    def test_numbers_type(self):
        self.assertIsInstance(numbers, dict)
