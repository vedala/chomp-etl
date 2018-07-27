import sys
import json
import db_postgres

def extract_data(config_dict):
    extract_location = config_dict['extract_folder']
    tables_list = config_dict['tables']
    for table_dict in tables_list:
        table_name = table_dict['name']
        columns = table_dict['columns']
        connect_string = table_dict['connect_string']
        db_postgres.fetch_and_write_data(table_name, columns,
                                connect_string, extract_location)
