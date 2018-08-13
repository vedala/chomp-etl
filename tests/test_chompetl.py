import unittest
from unittest.mock import patch, call
import os
import io
import sys
from chompetl import get_file_contents, check_args, main

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

    def test_main_if_check_args(self):
        """Does it exit with 1 if check_args fails?"""

        sys.argv[1:] = [1, 2, 3, 4]
        with self.assertRaises(SystemExit) as ctx:
            main()
        self.assertEqual(1, ctx.exception.code)

    @patch('chompetl.get_file_contents', side_effect=FileNotFoundError)
    @patch('chompetl.check_args', return_value=0)
    def test_main_credential_file_missing(self,
                                  mock_check_args, mock_get_file_contents):
        """Does it exit with 2 if get_file_contents raises error?"""

        sys.argv[1:] = ["", "a_file", "another_file"]
        with self.assertRaises(SystemExit) as ctx:
            main()
        self.assertEqual(2, ctx.exception.code)
        mock_check_args.assert_called_once()
        mock_get_file_contents.assert_called_once()


    @patch('json.loads')
    @patch('chompetl.check_args', return_value = 0)
    @patch('extract.extract')
    @patch('chompetl.get_file_contents')
    def test_main_get_file_contents_calls(self, mock_get_file_contents,
                              mock_extract, mock_check_args, mock_json_loads):
        """Is get_file_contents called twice with different arg each time?"""

        credentials_file = "a_file"
        source_cfg_file  = "another_file"
        sys.argv[1:] = ["", credentials_file, source_cfg_file, "", ""]
        main()
        expected_calls = [call(credentials_file), call(source_cfg_file)]
        mock_get_file_contents.assert_has_calls(expected_calls)


    @patch('chompetl.get_file_contents',
          side_effect=["first_call_return_string","second_call_return_string"])
    @patch('chompetl.check_args', return_value = 0)
    @patch('extract.extract')
    @patch('json.loads')
    def test_main_json_loads_calls(self, mock_json_loads, mock_extract,
                                    mock_check_args, mock_get_file_contents):
        """Is json_loads called twice with different arg each time?"""

        sys.argv[1:] = ["", "", "", "", ""]
        main()
        expected_calls = [call("first_call_return_string"),
                                            call("second_call_return_string")]
        mock_json_loads.assert_has_calls(expected_calls)

if __name__ == "__main__":
    unittest.main()
