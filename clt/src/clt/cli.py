"""
Script that implements the main function of the command line tools.

Contains:
    a function to parse command line arguments
    a main function that executes on calling script

"""

from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(prog='clt', description='A cli that implements common shell functions in python.')

    parser.add_argument('--echo', '-e', help='input message to the echoed')

    return parser


def main():
    """

    """
    from clt import echo

    args = create_parser().parse_args()

    echo.echo_msg(args.echo)
