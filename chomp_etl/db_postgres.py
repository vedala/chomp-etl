import psycopg2
import os
import csv

def fetch_and_write_data(table, columns, connect_string, extract_location):
    conn = psycopg2.connect(connect_string)
    cursor = conn.cursor()
    sql_str = construct_sql(table, columns)
    cursor.execute(sql_str)

    filename_with_path = construct_filename(extract_location, table)
    extract_file = open(filename_with_path, 'w+')
    csv_writer = csv.writer(extract_file, quotechar='"',
                                    quoting=csv.QUOTE_NONNUMERIC)

    for row in cursor:
        write_row_to_file(extract_file, csv_writer, row)

    extract_file.close()

def construct_filename(directory, base_filename):
    filename_with_path = os.path.join(os.path.expanduser(directory),
                                               base_filename + ".csv")
    return filename_with_path 

def write_row_to_file(file_obj, csv_writer, row):
    csv_writer.writerow(row)

def construct_sql(table, columns):
    col_str = ", ".join(columns)
    sql_str = f"SELECT {col_str} FROM {table}"
    return sql_str
