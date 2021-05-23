import unittest
from Q1 import Reverse, Reverse_sentence

class ReverseTest(unittest.TestCase):
    #Check Reverse function
    def test_reverse_word(self):
        w = 'Python'
        self.assertEqual(Reverse(w), "nohtyP")
    def test_split(self):
        s = 'Reverse Words'
        self.assertEqual(s.split(' '), ['Reverse', 'Words'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    #Check Reverse_sentence function
    def test_reverse_sent(self):
        s = 'Flipped class room'
        self.assertEqual(Reverse_sentence(s), "deppilF ssalc moor")

if __name__ == '__main__':
    unittest.main()