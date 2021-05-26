import unittest
import leap

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leap.year(3), 'No')
    def test2(self):
        self.assertEqual(leap.year(100), 'Yes')

if __name__ == '__main__':
    unittest.main()