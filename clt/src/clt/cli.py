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
    parser.add_argument('--rm',
                        help='remove a file or files'
                        )
    parser.add_argument('--dir',
                        choices=['True', 'False'],
                        help='used with --rm to indicate directory')
    parser.add_argument('--touch', '-t',
                        help='make a file')

    return parser


def main():
    """

    """
    from clt import shell_functions

    args = create_parser().parse_args()

    if args.mkdir:
        shell_functions.make_directory(args.mkdir)
    elif args.echo:
        shell_functions.echo_msg(args.echo)
    elif args.rm:
        shell_functions.remove_file(args.rm, args.dir)
    elif args.touch:
        shell_functions.touch_file(args.touch)
