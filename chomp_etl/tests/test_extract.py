import unittest
from extract import yaml_str_to_dict

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

if __name__ == "__main__":
    unittest.main()
