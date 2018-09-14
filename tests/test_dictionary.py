from dictionary import returnDict
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        self.numbers = returnDict()
         
    def test_return_dict(self):
        self.assertEqual(len(self.numbers), 15)
    
    def test_keys(self):
        self.assertEqual(self.numbers[1], 1)
        self.assertEqual(self.numbers[2], 4)
        self.assertEqual(self.numbers[5], 25)

    def test_numbers_type(self):
        self.assertIsInstance(self.numbers, dict)
    
    def testReturndict(self):
        self.assertEqual(returnDict(), self.numbers)
