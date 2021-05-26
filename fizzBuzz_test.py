import unittest
import code

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(code.printFB(3), 'Fizz')
    def test2(self):
        self.assertEqual(code.printFB(5), 'Buzz')
    def test3(self):
        self.assertEqual(code.printFB(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()