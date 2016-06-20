import unittest
import CrimeNearSchool
import os


class Test(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

    def assertMultiLineEqual(self, first, second, msg=None):
     """Assert that two multi-line strings are equal.

    If they aren't, show a nice diff.

    """
    self.assertTrue(isinstance(first, str),
                    'First argument is not a string')
    self.assertTrue(isinstance(second, str),
                    'Second argument is not a string')

    if first != second:
        message = ''.join(difflib.ndiff(first.splitlines(True),
                                        second.splitlines(True)))
        if msg:
            message += " : " + msg
        self.fail("Multi-line strings are unequal:\n" + message)

if __name__ == '__main__':
    unittest.main()
