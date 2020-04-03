def local(infile, outfile):
    """
    Creates a local backup of a file. Takes two open files as inputs.

    How would I test this? I.e. in the case the file is not open already?
    """

    outfile.write(infile.read())
    outfile.close()
    infile.close()

