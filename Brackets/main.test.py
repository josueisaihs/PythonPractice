import unittest

from main import BracketSentinel as BS

class MainTest(unittest.TestCase):
    c = "{()([{{()}()()[[[[[]]]]]}])}"
    d = "{{([)]}}"
    e = ""
    f = "{"
    r = "}"
    h = "()()(){[{]}]}"

    def test_brackets(self):
        bs = BS()
        self.assertTrue(bs.run(brackets = self.e))

    def test_brackets_false(self):
        bs = BS()
        self.assertFalse(bs.run(brackets = self.r))

    def test_sentinel(self):
        bs = BS()
        self.assertTrue(bs.sentinel(brackets = self.c))

    def test_sentinel_false(self):
        bs = BS()
        self.assertFalse(bs.sentinel(brackets = self.h))

if __name__ == "__main__":
    unittest.main()