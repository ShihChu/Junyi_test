import unittest
from Q2 import Count

class CountTest(unittest.TestCase):
    #Check Count function
    def test_count(self):
        n = 15
        self.assertEqual(Count(n), 9)
        

if __name__ == '__main__':
    unittest.main()
