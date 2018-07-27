import unittest
import os
from extract import main, get_file_contents

class IntegrationPostgresExtractTestCase(unittest.TestCase):
    """Tests for extracting from postgresql."""

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

if __name__ == "__main__":
    unittest.main()
