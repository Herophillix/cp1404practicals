"""
Sort the files by user choice
"""
import os
import shutil


def main():
    """Sort the files by user choice"""
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

    user_file_types = {}
    for extension_type in file_extensions.keys():
        file_type = input("What category would you like to sort {0} files into? ".format(extension_type))
        while file_type == "":
            print("Input cannot be empty")
            file_type = input("What category would you like to sort {0} files into? ".format(extension_type))
        if file_type not in user_file_types:
            user_file_types[file_type] = file_extensions[extension_type]
        else:
            user_file_types[file_type] += file_extensions[extension_type]

    for user_file_type, files in user_file_types.items():
        try:
            os.mkdir(user_file_type)
        except FileExistsError:
            pass
        for filename in files:
            shutil.move(filename, '{0}/'.format(user_file_type) + filename)


if __name__ == "__main__":
    main()
