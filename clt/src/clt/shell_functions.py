import os

def make_directory(path):
    os.mkdir(path)

def echo_msg(msg):

    print(msg)

def remove_file(files):
    """
    Remove a file or path. Will catch errors if a directory is passed.

    """
    try:
        os.remove(files)
    except OSError as error:
        print(error)
        print('Use -r=True option to remove directories.')
