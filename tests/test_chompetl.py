import unittest
import os
import io
import sys
from chompetl import get_file_contents, check_args

class ChompetlTestCase(unittest.TestCase):
    """Tests for `extract.py`."""

    def test_get_file_contents_invalid_file(self):
        """Does it raise error when unable to open file?"""

        filename = "this_file_does_not_exist.txt"
        printCapture = io.StringIO()
        sys.stderr = printCapture
        self.assertRaises(FileNotFoundError, get_file_contents, filename)
        sys.stderr = sys.__stderr__
        self.assertEqual(
            'Error, file "this_file_does_not_exist.txt" does not exist.\n',
            printCapture.getvalue())

    def test_get_file_contents_valid_file(self):
        """Does it return file contents?"""

        filename_with_path = os.path.join(
                                 os.path.expanduser('~/misc/extract_out'),
                                 'afile.txt')
        contents = "some-content-line-1\nsome-content-line-2"
        with open(filename_with_path, 'w+') as f:
            f.write(contents)

        contents_received = get_file_contents(filename_with_path)
        self.assertEqual(contents, contents_received)

    def test_check_args_incorrect_args(self):
        """Does it return 1 when incorrect num of arguments supplied?"""

        expected_string = \
            "Incorrect number of arguments. Five arguments expected.\n"   \
            "Usage: chomp_etl <source_type> <credentials_file>  "         \
            "<source_config_file> <extract_location> <extract_filename>\n"

        printCapture = io.StringIO()
        sys.stderr = printCapture
        retval = check_args([1, 2, 3, 4, 5])
        self.assertEqual(1, retval)
        self.assertEqual(expected_string, printCapture.getvalue())
        sys.stderr = sys.__stderr__

        printCapture = io.StringIO()
        sys.stderr = printCapture
        retval = check_args([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(1, retval)
        self.assertEqual(expected_string, printCapture.getvalue())
        sys.stderr = sys.__stderr__

    def test_check_args_correct_args(self):
        """Does it return 0 when correct num of arguments supplied?"""

        retval = check_args([1, 2, 3, 4, 5, 6])
        self.assertEqual(0, retval)

if __name__ == "__main__":
    unittest.main()
