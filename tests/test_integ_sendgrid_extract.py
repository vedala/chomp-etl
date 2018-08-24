import unittest
import os
import sys
from chompetl import main, get_file_contents

class IntegrationSendgridExtractTestCase(unittest.TestCase):
    """Tests for extracting from sendgrid."""

    def test_sendgrid_extract(self):
        """Does extract from sendgrid create expected output files?"""

        source_type = "sendgrid"
        credentials = "sendgrid_credentials.json"
        config_file = "sendgrid_config.json"
        extract_folder =  "~/misc/extract_out"
        extract_filename = "sendgrid_out"
        sys.argv[1:] = [source_type, credentials, config_file,
                                          extract_folder, extract_filename]

        main()
        expected_str = (
            "\"2018-07-01\",0,0,0\n"
            "\"2018-07-02\",0,0,0\n"
            "\"2018-07-03\",0,0,0\n"
            "\"2018-07-04\",0,0,0\n"
            "\"2018-07-05\",0,0,0\n"
            "\"2018-07-06\",0,0,0\n"
            "\"2018-07-07\",0,0,0\n"
            "\"2018-07-08\",0,0,0\n"
            "\"2018-07-09\",0,0,0\n"
            "\"2018-07-10\",0,0,0\n"
            "\"2018-07-11\",0,0,0\n"
            "\"2018-07-12\",0,0,0\n"
            "\"2018-07-13\",0,0,0\n"
            "\"2018-07-14\",0,0,0\n"
            "\"2018-07-15\",0,0,0\n"
            "\"2018-07-16\",0,0,0\n"
            "\"2018-07-17\",0,0,0\n"
            "\"2018-07-18\",0,0,0\n"
            "\"2018-07-19\",0,0,0\n"
            "\"2018-07-20\",0,0,0\n"
            "\"2018-07-21\",0,0,0\n"
            "\"2018-07-22\",0,0,0\n"
            "\"2018-07-23\",0,0,0\n"
            "\"2018-07-24\",0,0,0\n"
            "\"2018-07-25\",0,0,0\n"
            "\"2018-07-26\",0,0,0\n"
            "\"2018-07-27\",0,0,0\n"
            "\"2018-07-28\",0,0,0\n"
            "\"2018-07-29\",0,0,0\n"
            "\"2018-07-30\",3,1,1\n"
            "\"2018-07-31\",0,0,0\n"
            "\"2018-08-01\",0,0,0\n"
            "\"2018-08-02\",0,0,0\n"
            "\"2018-08-03\",0,0,0\n"
            "\"2018-08-04\",0,0,0\n"
            "\"2018-08-05\",0,0,0\n"
            "\"2018-08-06\",0,0,0\n"
            "\"2018-08-07\",0,0,0\n"
            "\"2018-08-08\",0,0,0\n"
            "\"2018-08-09\",0,0,0\n"
            "\"2018-08-10\",0,0,0\n"
            "\"2018-08-11\",0,0,0\n"
            "\"2018-08-12\",0,0,0\n"
            "\"2018-08-13\",0,0,0\n"
            "\"2018-08-14\",0,0,0\n"
            "\"2018-08-15\",0,0,0\n"
            "\"2018-08-16\",0,0,0\n"
            "\"2018-08-17\",15,15,11\n"
            "\"2018-08-18\",0,0,0\n"
            "\"2018-08-19\",0,0,4\n"
            "\"2018-08-20\",0,0,0\n"
            "\"2018-08-21\",0,0,0\n"
        )

        test_file_1 = "~/misc/extract_out/sendgrid_out.csv"
        self.assertEqual(expected_str,
                            get_file_contents(os.path.expanduser(test_file_1)))
        os.remove(os.path.expanduser(test_file_1))

if __name__ == "__main__":
    unittest.main()
