"""
Script that implements the main function of the command line tools.

Contains:
    a function to parse command line arguments
    a main function that executes on calling script

"""

from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(prog='clt',
                            description='A cli that implements common shell functions in python.')

    parser.add_argument('--echo',
                        '-e',
                        help='input message to the echoed')
    parser.add_argument('--mkdir',
                        help='input name of file or path'
                        )

    return parser


def main():
    """

    """
    from clt import echo, make_directory

    args = create_parser().parse_args()

    if args.mkdir:
        make_directory(args.mkdir)
    elif args.echo:
        echo.echo_msg(args.echo)
