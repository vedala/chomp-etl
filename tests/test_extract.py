import unittest
import os
from extract import construct_filename

class ExtractTestCase(unittest.TestCase):
    """Tests for `extract.py`."""

    def test_construct_filename(self):
        """Is returning correct filename with full path?"""

        directory = "~/misc/extract_out"
        file_base = "myoutfile"
        expected_string = os.path.join(os.path.expanduser(directory),
                                                    file_base + ".csv")
        self.assertEqual(expected_string,
                                construct_filename(directory, file_base))

if __name__ == "__main__":
    unittest.main()
