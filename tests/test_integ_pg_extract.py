import unittest
import os
import sys
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

        source_type = "postgres"
        credentials = "pg_credentials.json"
        config_file = "job_1001.json"
        extract_folder =  "~/misc/extract_out"
        extract_filename = "job_1001_out"
        sys.argv[1:] = [source_type, credentials, config_file,
                                          extract_folder, extract_filename]

        main()
        expected_str_customers = '"John","Smith",30301\n"Kim","Hunter",30302\n'
        test_file_1 = "~/misc/extract_out/job_1001_out.csv"
        self.assertEqual(expected_str_customers,
                            get_file_contents(os.path.expanduser(test_file_1)))
        os.remove(os.path.expanduser(test_file_1))

if __name__ == "__main__":
    unittest.main()
