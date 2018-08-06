import unittest
import os
from chompetl import get_extract_config, check_args, get_file_contents
import json

class ExtractTestCase(unittest.TestCase):
    """Tests for `extract.py`."""

    def test_get_config_dict(self):
        """Is json string correctly converted to dictionary?"""

        json_str = '{"config_str": "somestring", "config_list": [ "item_1", "item_2"]}'
        expected_dictionary = {'config_list': ['item_1', 'item_2'],
                                         'config_str': 'somestring'}
        my_dictionary = get_extract_config(json_str)
        self.assertEqual(expected_dictionary, my_dictionary)

    def test_json_str_to_dict_empty_input(self):
        """Does empty json string raise exception?"""

        json_str = ""
        with self.assertRaises(json.decoder.JSONDecodeError):
            get_extract_config(json_str)

    def test_check_args_too_few_args(self):
        """Is returning non-zero value if too few arguments?"""
        my_argv = ["extract"]
        self.assertNotEqual(0, check_args(my_argv))

    def test_check_args_too_many_args(self):
        """Is returning non-zero value if too many arguments?"""
        my_argv = ["extract", "arg1", "arg2"]
        self.assertNotEqual(0, check_args(my_argv))

    def test_get_file_contents_non_existent(self):
        """Is raising FileNotFoundError for non-existent file?"""
        with self.assertRaises(FileNotFoundError):
            get_file_contents("no_such_file.txt")

    def test_get_file_contents(self):
        """Is returning contents of the file?"""

        test_file = "a_test_file.txt"
        with open(test_file, 'w') as f:
            f.write("contents-line-1\n")
            f.write("contents-line-2\n")
            f.write("contents-line-3\n")

        expected_string = "contents-line-1\ncontents-line-2\ncontents-line-3\n"
        self.assertEqual(expected_string, get_file_contents(test_file))
        os.remove(test_file)

if __name__ == "__main__":
    unittest.main()
