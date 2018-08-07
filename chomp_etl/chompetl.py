import sys
import json
import extract

def main():
    argv = sys.argv
    if check_args(argv):
        sys.exit(1)

    try:
        source_type = argv[1]
        credentials = get_file_contents(argv[2])
        source_config_json = get_file_contents(argv[3])
    except FileNotFoundError:
        sys.exit(2)

    source_config = json.loads(source_config_json)
    extract_location = argv[4]
    extract_filename = argv[5]
    extract.extract(source_type, credentials, source_config,
                                          extract_location, extract_filename)

def check_args(argv):
    num_args = len(argv)
    if num_args != 6:
        print("Incorrect number of arguments. Five arguments expected.",
                                                        file=sys.stderr)
        print(
            f"Usage: {argv[0]} <source_type> <credentials_file> "
            " <source_config_file> <extract_location> <extract_filename>",
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
