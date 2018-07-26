import unittest
import yaml
from db_postgres import fetch_and_print_data, construct_sql

class DbPostgresTestCase(unittest.TestCase):
    """Tests for `db_postgres.py`."""

    def test_construct_sql(self):
        """Is sql correctly constructed from table and column names?"""
        table = "customers"
        columns = ['name', 'address', 'phone']
        sql_str = "SELECT name, address, phone FROM customers"
        self.assertEqual(sql_str, construct_sql(table, columns))

if __name__ == "__main__":
    unittest.main()
