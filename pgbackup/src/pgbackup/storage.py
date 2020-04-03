def local(infile, outfile):
    """
    Creates a local backup of a file. Takes two open files as inputs.

    How would I test this? I.e. in the case the file is not open already?
    """

    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    """
    Uploads an infile to S3. Will accept any client object that uses an upload_fileobj method.

    upload_fileobj accepts bytes objects
    """

    client.upload_fileobj(infile, bucket, name)
