import unittest
import leap

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leap.year(3), 'No')

if __name__ == '__main__':
    unittest.main()