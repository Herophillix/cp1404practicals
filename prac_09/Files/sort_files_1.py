"""
Sort the files given into its corresponding file type
"""
import os
import shutil


def main():
    """Sort the files given into its corresponding file type"""
    os.chdir("FilesToSort")
    file_extensions = {}

    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        split_filename = filename.split('.')
        if len(split_filename) == 2:
            extension_type = split_filename[1]
            if extension_type not in file_extensions:
                file_extensions[extension_type] = [filename]
            else:
                file_extensions[extension_type].append(filename)

    for extension_type, files in file_extensions.items():
        try:
            os.mkdir(extension_type)
        except FileExistsError:
            pass
        for filename in files:
            shutil.move(filename, '{0}/'.format(extension_type) + filename)


if __name__ == "__main__":
    main()
