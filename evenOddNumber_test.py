import unittest


from evenOddNumber import evenOddNumber


class EvenOddNumber(unittest.TestCase):
    def testEvenNumber(self):
        self.assertTrue(evenOddNumber(8))

    def testOddNumber(self):
        self.assertFalse(evenOddNumber(5))