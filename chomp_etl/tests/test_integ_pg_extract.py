import unittest
import os
from chompetl import main, get_file_contents

class IntegrationPostgresExtractTestCase(unittest.TestCase):
    """Tests for extracting from postgresql."""

    def count_lines(self, file_name):
        count = 0
        with open(file_name) as f:
            while True:
                row = f.readline()
                if not row:
                    break
                count = count + 1
        return count

    def test_postgres_extract(self):
        """Does extract from postgres create expected output files?"""

        json_file = "job_1001.json"

        main(["", json_file])
        expected_str_customers = '"John","Smith",30301\n"Kim","Hunter",30302\n'
        expected_str_stores = '"Atlanta",5000\n"Sandy Springs",8000\n'
        test_file_1 = "~/misc/extract_out/customers.csv"
        test_file_2 = "~/misc/extract_out/stores.csv"
        self.assertEqual(expected_str_customers,
                            get_file_contents(os.path.expanduser(test_file_1)))
        self.assertEqual(expected_str_stores,
                            get_file_contents(os.path.expanduser(test_file_2)))
        os.remove(os.path.expanduser(test_file_1))
        os.remove(os.path.expanduser(test_file_2))

    def test_postgres_extract_job_1002(self):
        """Does extract from postgres create expected number of rows?"""

        json_file = "job_1002.json"
        main(["", json_file])
        test_file_1 = "~/misc/extract_out/customers2.csv"
        test_file_2 = "~/misc/extract_out/stores2.csv"
        expected_customers_count = 30
        expected_stores_count = 20
        file_1_lines = self.count_lines(os.path.expanduser(test_file_1))
        file_2_lines = self.count_lines(os.path.expanduser(test_file_2))
        self.assertEqual(expected_customers_count, file_1_lines)
        self.assertEqual(expected_stores_count, file_2_lines)
        os.remove(os.path.expanduser(test_file_1))
        os.remove(os.path.expanduser(test_file_2))

if __name__ == "__main__":
    unittest.main()
