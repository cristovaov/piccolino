import argparse
import sys

from piccolino import __version__


def parse_arguments():
    """

    :return:
    """
    parser = argparse.ArgumentParser(prog='piccolino')

    parser.add_argument(dest='source_directory', nargs='?', help='source files directory')

    return parser.parse_args()


def main():
    """

    """
    if not len(sys.argv) > 1:
        print("{} {}".format(__package__, __version__))
        print("Type -h or --help for usage instructions.")
    else:
        print(parse_arguments())

    # try:
    #     if not len(sys.argv) > 1:
    #         print("{} {}".format(__package__, __version__))
    #         print("Type -h or --help for usage instructions.")
    #     else:
    #         print(parse_arguments())
    # except:
    #     pass

