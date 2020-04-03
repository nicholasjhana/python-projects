import subprocess
import sys

def dump(url):
    """
    Runs subprocess Popen to run the pg dump command

    Uses basic error handling to catch for if pg_dump isn't installed.
    """

    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)


def dump_file_name(url, timestamp=None):
    #split on the url slashes taking the last element
    #then split on the query strings taking the first item to get the db name
    db_name = url.split('/')[-1]
    db_name = db_name.split('?')[0]

    if timestamp:
        return f'{db_name}-{timestamp}.sql'
    else:
        return f'{db_name}.sql'
