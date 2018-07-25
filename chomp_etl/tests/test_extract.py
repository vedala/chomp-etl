import unittest
from extract import yaml_str_to_dict, check_args

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

    def test_check_args_too_few_args(self):
        """Is returning non-zero value if too few arguments?"""
        my_argv = ["extract"]
        self.assertNotEqual(0, check_args(my_argv))

    def test_check_args_too_many_args(self):
        """Is returning non-zero value if too many arguments?"""
        my_argv = ["extract", "arg1", "arg2"]
        self.assertNotEqual(0, check_args(my_argv))

if __name__ == "__main__":
    unittest.main()
