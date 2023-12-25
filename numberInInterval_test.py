import unittest

from numberInInterval import numberInInterval


class NumberInInterval(unittest.TestCase):
    def testInInterval(self):
        self.assertTrue(numberInInterval(27))

    def testIsNotInterval(self):
        self.assertFalse(numberInInterval(15))

    def testGreatInterval(self):
        self.assertFalse(numberInInterval(200))