import zipfile


def extract_archive(archivepath, dest_dir):
    # When we want to create the ZipFile we use write or 'w'
    # On the other hand, when we want to see the content of the ZipFile
    # We use the read 'r' option

    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__== "__main__":
    extract_archive('compressed.zip', dest_dir='./')

