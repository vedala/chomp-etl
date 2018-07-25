import sys
import yaml

def main(argv):
    my_dict = yaml.load(open('example_job.yaml'))
    return my_dict

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args < 2:
        print("Too few arguments. One argument expected.")
        sys.exit(1)
    elif num_args > 2:
        print("Too many arguments. Only one argument expected.")
        sys.exit(2)

    print(main(sys.argv[1]))
