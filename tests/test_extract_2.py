import unittest
from unittest.mock import patch
import extract
import source_postgres

class ExtractTestCase(unittest.TestCase):
    """Tests file 2 for `extract.py`."""

    def mocked_get_batch(self):
        """Serves two batches and then serves empty list in third call."""

        if hasattr(self, 'batch_count'):
            self.batch_count += 1
        else:
            self.batch_count = 1

        batch_1 = [(1, "aaa", 1000), (2, "bbb", 2000)]
        batch_2 = [(3, "ccc", 3000), (4, "ddd", 4000)]
        empty_batch = []

        if self.batch_count == 1:
            return batch_1
        elif self.batch_count == 2:
            return batch_2
        else:
            return empty_batch

    @patch.object(source_postgres.SourcePostgres, '__init__', lambda slf, cred, config: None)
    @patch.object(source_postgres.SourcePostgres, 'get_batch', mocked_get_batch)
    @patch.object(source_postgres.SourcePostgres, 'cleanup', lambda slf: [])
    @patch('extract.construct_filename')
    @patch('extract.write_batch')
    def test_extract_function(self, mock_write_batch, mock_construct_fn):
        source_type = "postgres"
        credentials = {'dbname': 'somedb', 'user':'someuser'}
        source_config = {'table': 'sometable', 'key2': 'somevalue'}
        extract_location = "/some/path"
        extract_filename = "a_file"
        extract.extract(source_type, credentials, source_config,
                                     extract_location, extract_filename)
        self.assertEqual(2, mock_write_batch.call_count)
        mock_construct_fn.assert_called_once()
        mock_construct_fn.assert_called_once_with(extract_location, extract_filename)
        

if __name__ == "__main__":
    unittest.main()
