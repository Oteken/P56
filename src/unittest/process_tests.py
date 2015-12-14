import sys
import datetime
import unittest
sys.path.insert(0, '../main/python')

import Process

class TestMyFunctions(unittest.TestCase):
    def test_string_to_date(self):
        self.assertEqual(Process.stringToDate("2015-03-10 00:47:24"),
                                              datetime.datetime(2015,3,10,0,47,24))

if __name__ == '__main__':
    unittest.main(exit=False)