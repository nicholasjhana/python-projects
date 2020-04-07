"""
Script that implements the main function of the command line tools.

Contains:
    a function to parse command line arguments
    a main function that executes on calling script

"""

from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(prog='echo')

    parser.add_argument('message', help='input message to the echoed')

    return parser


def main():
    """

    """
    from echo import echo_msg

    args = create_parser().parse_args()

    echo_msg(args.message)
