import unittest
import os
from extract import construct_filename, write_batch
from chompetl import get_file_contents

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

    def test_write_batch(self):
        """Is writing batch data to file_object?"""

        directory = "~/misc/extract_out"
        file_base = "abatchfile.csv"
        file_with_path = os.path.join(os.path.expanduser(directory),
                                                    file_base + ".csv")
        file_object = open(file_with_path, "w+")
        batch = [(1,"aaa",100),(2,"bbb",200)]
        write_batch(file_object, batch)
        file_object.close()

        file_contents = get_file_contents(file_with_path)
        expected_string = '1,"aaa",100\n2,"bbb",200\n'
        self.assertEqual(expected_string, file_contents)

if __name__ == "__main__":
    unittest.main()
