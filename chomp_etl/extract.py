import sys
import yaml

def main(argv):
    num_args = len(sys.argv)
    if num_args < 2:
        print("Too few arguments. One argument expected.", file=sys.stderr)
        sys.exit(1)
    elif num_args > 2:
        print("Too many arguments. Only one argument expected.", file=sys.stderr)
        sys.exit(2)

    return read_yaml(argv[1])

def read_yaml(filename):
    my_dict = yaml.load(open(filename))
    return my_dict


if __name__ == "__main__":
    print(main(sys.argv))
