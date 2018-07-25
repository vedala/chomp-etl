import sys
import yaml

def main(argv):
    my_dict = yaml.load(open('example_job.yaml'))
    return my_dict

if __name__ == "__main__":
    print(main(sys.argv[1]))
