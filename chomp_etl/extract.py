import sys
import yaml

def main(argv):
    check_args(argv)

    try:
        file_contents = get_file_contents(argv[1])
    except FileNotFoundError:
        sys.exit(3)

    return yaml_str_to_dict(file_contents)

def check_args(argv):
    num_args = len(argv)
    if num_args < 2:
        print("Too few arguments. One argument expected.", file=sys.stderr)
        sys.exit(1)
    elif num_args > 2:
        print("Too many arguments. Only one argument expected.", file=sys.stderr)
        sys.exit(2)

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
    print(main(sys.argv))
