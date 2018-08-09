import os
import csv
from source_postgres import SourcePostgres

def extract(source_type, credentials, source_config,
                                    extract_location, extract_filename):
    if source_type == 'postgres':
        source = SourcePostgres(credentials, source_config)
    else:
        raise Exception("Invalid source_type specified.")

    filename_with_path = construct_filename(extract_location, extract_filename)
    file_obj = open(filename_with_path, 'w+')
    while True:
        data_batch = source.get_batch()
        if len(data_batch) == 0:
            break
        write_batch(file_obj, data_batch)

    file_obj.close()
    source.cleanup()

def write_batch(file_obj, data_batch):
    csv_writer = csv.writer(file_obj, quotechar='"',
                                      quoting=csv.QUOTE_NONNUMERIC)
    for row in data_batch:
        csv_writer.writerow(row)

def construct_filename(directory, base_filename):
    filename_with_path = os.path.join(os.path.expanduser(directory),
                                               base_filename + ".csv")
    return filename_with_path
