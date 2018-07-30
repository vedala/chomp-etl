import db_postgres
import api_sendgrid

def extract_data(config_dict):
    extract_source = config_dict['extract_source']
    if extract_source == 'postgres':
        extract_postgres(config_dict)
    elif extract_source == 'sendgrid':
        extract_sendgrid(config_dict)


def extract_sendgrid(config_dict):
    extract_location = config_dict['extract_folder']
    api_key = config_dict['api_key']
    fields = config_dict['stats']['fields']
    start_date = config_dict['stats']['start_date']
    end_date = config_dict['stats']['end_date']
    api_sendgrid.fetch_and_write_data('stats', api_key, fields, start_date,
                                            end_date, extract_location)

def extract_postgres(config_dict):
    extract_location = config_dict['extract_folder']
    tables_list = config_dict['tables']
    for table_dict in tables_list:
        table_name = table_dict['name']
        columns = table_dict['columns']
        connect_string = table_dict['connect_string']
        if 'fetch_rows' in table_dict:
            num_fetch_rows = table_dict['fetch_rows']
        else:
            num_fetch_rows = None
        db_postgres.fetch_and_write_data(table_name, columns,
                            connect_string, extract_location, num_fetch_rows)
