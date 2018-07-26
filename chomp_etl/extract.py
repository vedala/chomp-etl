import sys
import yaml
import db_postgres

def main(argv):
    if check_args(argv):
        sys.exit(1)

    try:
        file_contents = get_file_contents(argv[1])
    except FileNotFoundError:
        sys.exit(2)

    config_dict = yaml_str_to_dict(file_contents)
    extract_data(config_dict)

def extract_data(config_dict):
    extract_location = config_dict['extract_folder']
    tables_list = config_dict['tables']
    for table_dict in tables_list:
        table_name = table_dict['name']
        columns = get_column_list(table_dict['columns'])
        connect_string = table_dict['connect_string']
        db_postgres.fetch_and_write_data(table_name, columns,
                                connect_string, extract_location)

def get_column_list(columns_yaml_list):
    column_list = []
    for item in columns_yaml_list:
        column_list.append(item['column_name'])
    return column_list

def check_args(argv):
    num_args = len(argv)
    if num_args < 2:
        print("Too few arguments. One argument expected.", file=sys.stderr)
        return 1
    elif num_args > 2:
        print("Too many arguments. Only one argument expected.",
                                                          file=sys.stderr)
        return 1

    return 0

def get_file_contents(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Error, file "{filename}" does not exist.', file=sys.stderr)
        raise

    return contents

def yaml_str_to_dict(yaml_str):
    my_dict = yaml.load(yaml_str)
    return my_dict

if __name__ == "__main__":
    main(sys.argv)
