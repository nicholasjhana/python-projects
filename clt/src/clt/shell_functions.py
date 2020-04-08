import os

def make_directory(path):
    os.mkdir(path)

def echo_msg(msg):
    print(msg)

def remove_file(files, dir=False):
    """
    Remove a file or path. Will catch errors if a directory is passed.

    """
    if dir:
        os.rmdir(files)
    else:
        try:
            os.remove(files)
        except OSError as error:
            print(error)
            print('Use -dir=True option to remove directories.')

def touch_file(file_name):

    open(file_name, 'w').close()
