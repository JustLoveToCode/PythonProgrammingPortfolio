import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # We are creating a Zip file, hence it is write 'w' mode
    # If you want to extract the zip file, it is 'r' mode
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # the filepaths is referring to the "todos.txt" and the "experiment.py"
        # Using the for loop to loop through the filepaths
        # We get the Specific Instance of the filepath

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            # This will extract only the name of that path using the arcname=filepath.name
            archive.write(filepath, arcname=filepath.name)


# If your zipCreator.py is in the Same Directory as your todos.txt and experiment.py
# If your destination path of your files is totally Different Directory from your zipCreator.py file

# Testing your code in the Backend by using the __name__="__main__":
if __name__ == "__main__":
    # This is invoking the function above by putting in the argument for the file
    # ./ will create the file in the LewPython, ./ mean moving out of the zipCreator.py
    make_archive(filepaths=["todos.txt", "experiment.py"], dest_dir='./')
