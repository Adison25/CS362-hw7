import unittest
import code

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(code.printFB(3), 'Fizz')

if __name__ == '__main__':
    unittest.main()