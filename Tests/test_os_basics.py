import unittest
import os
import tempfile

from os_basics import change_dir

class OsBasicsTestCases(unittest.TestCase):
    """Tests for 'os_basics.py'."""

    def test_change_dir(self):
        """Have we changed directory locations?"""
        test_dir = tempfile.mkdtemp('TempDir')
        change_dir(test_dir)
        self.assertEquals(os.getcwd(), test_dir)
      
      
if __name__ == '__main__':
    unittest.main()