import os
import sys
import tempfile
import unittest

from os_basics import change_dir
from os_basics import exit_program
from os_basics import open_file

class OsBasicsTestCases(unittest.TestCase):
    """Tests for 'os_basics.py'."""

    def test_change_dir(self):
        """Have we changed directory locations?"""
        test_dir = tempfile.mkdtemp()
        change_dir(test_dir)
        self.assertEqual(os.getcwd(), test_dir)
        change_dir('Tests')
        self.assertEqual(os.getcwd(), test_dir)
        os.rmdir(test_dir)
      
      
    def test_exit_program(self):
        """Does the program display a message and then exit?"""
        msg = "Test message"
        with self.assertRaises(SystemExit):
            exit_program(msg)


    def test_open_file(self):
        """Is the file opened correctly?"""
        test_file = tempfile.mkstemp()
        f = open_file(test_file[1])
        self.assertTrue(f.readable())
        f.close()
        os.close(test_file[0])
        os.remove(test_file[1])

        test_file = ''
        with self.assertRaises(FileNotFoundError):
            open_file(test_file)


if __name__ == '__main__':
    unittest.main()
