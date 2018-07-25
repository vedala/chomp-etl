import unittest
import os
from extract import yaml_str_to_dict, check_args, get_file_contents

class ExtractTestCase(unittest.TestCase):
    """Tests for `extract.py`."""

    def test_yaml_str_to_dict(self):
        """Is yaml string correctly converted to dictionary?"""

        yaml_str = """
        config_str: somestring
        config_list:
        - item_1
        - item_2
        """
        expected_dictionary = {'config_list': ['item_1', 'item_2'],
                                         'config_str': 'somestring'}
        my_dictionary = yaml_str_to_dict(yaml_str)
        self.assertEqual(expected_dictionary, my_dictionary)

    def test_yaml_str_to_dict_empty_input(self):
        """Is empty string converted to None?"""

        yaml_str = ""
        self.assertEqual(None, yaml_str_to_dict(yaml_str))

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
