import unittest
from unittest.mock import patch
import extract
import source_postgres
from io import IOBase

class MockedClose(object):
    def close(self):
        pass

class ExtractTestCase(unittest.TestCase):
    """Tests file 2 for `extract.py`."""

    filename_constructed = "/the/path/returned/xyz.txt"

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

    @patch.object(source_postgres.SourcePostgres,
                                    'get_batch', mocked_get_batch)
    @patch('builtins.open', return_value=MockedClose())
    @patch('extract.construct_filename', return_value=filename_constructed)
    @patch('extract.write_batch')
    @patch.object(source_postgres.SourcePostgres, 'cleanup')
    @patch.object(source_postgres.SourcePostgres, '__init__')
    def test_extract_function(self, mock_init, mock_cleanup, mock_write_batch,
                                                mock_construct_fn, mock_open):

        #
        # set mock_init's return_value to None, since this method is mocking
        # a constructor and constructor is required to return None
        #
        mock_init.return_value = None

        source_type = "postgres"
        credentials = {'dbname': 'somedb', 'user':'someuser'}
        source_config = {'table': 'sometable', 'key2': 'somevalue'}
        extract_location = "/some/path"
        extract_filename = "a_file"
        extract.extract(source_type, credentials, source_config,
                                     extract_location, extract_filename)

        #
        # verify call to open()
        #
        expected_filename_with_path = self.filename_constructed
        mock_open.assert_called_once_with(expected_filename_with_path, "w+")

        #
        # verify call to construct_function()
        #
        mock_construct_fn.assert_called_once_with(extract_location,
                                                        extract_filename)

        #
        # verify calls to write_batch()
        #
        self.assertEqual(2, mock_write_batch.call_count)

        write_batch_calls = [(1, 2), (3, 4)]
        write_batch_call_list = mock_write_batch.call_args_list

        first_call = write_batch_call_list[0]
        first_call_args, first_call_kwargs = first_call
        first_call_args_of_interest = first_call_args[1]

        second_call = write_batch_call_list[1]
        second_call_args, second_call_kwargs = second_call
        second_call_args_of_interest = second_call_args[1]

        self.assertEqual(first_call_args_of_interest,
                                    [(1, "aaa", 1000), (2, "bbb", 2000)])
        self.assertEqual(second_call_args_of_interest,
                                    [(3, "ccc", 3000), (4, "ddd", 4000)])

        #
        # verify call to cleanup()
        #
        mock_cleanup.assert_called_once_with()

        #
        # verify class constructor called with expected arguments
        #
        mock_init.assert_called_once_with(credentials, source_config)

if __name__ == "__main__":
    unittest.main()
