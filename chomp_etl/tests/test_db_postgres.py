import unittest
import yaml
from db_postgres import fetch_and_write_data, construct_sql
from extract import get_file_contents
import os

class DbPostgresTestCase(unittest.TestCase):
    """Tests for `db_postgres.py`."""

    def test_construct_sql(self):
        """Is sql correctly constructed from table and column names?"""
        table = "customers"
        columns = ['name', 'address', 'phone']
        sql_str = "SELECT name, address, phone FROM customers"
        self.assertEqual(sql_str, construct_sql(table, columns))

    def test_fetch_and_write_data(self):
        table = "tab1"
        columns = ['col1', 'col2']
        connect_str_from_yaml = get_file_contents('db_info.yaml')
        connect_string_dict = yaml.load(connect_str_from_yaml)
        connect_string = ""
        for k, v in connect_string_dict.items():
            connect_string = connect_string + k + "='"
            connect_string = connect_string + v + "' "
        extract_location = "~/misc/extract_out"
        fetch_and_write_data(table, columns, connect_string, extract_location)
        expected_str = '1,"AAA"\n2,"BBB"\n'
        extract_file = os.path.join(os.path.expanduser(extract_location),
                                                          table + ".csv")
        self.assertEqual(expected_str, get_file_contents(extract_file))

if __name__ == "__main__":
    unittest.main()
