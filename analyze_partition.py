import math
import os
import pprint
import sys


def convert_size(size_in_bytes):
    if size_in_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    power = math.pow(1024, i)
    result = round(size_in_bytes / power, 2)
    return "%.2f %s" % (result, size_name[i])


def partition_analysis(partition):
    extensions = set()
    extension_dict = {}
    file_size_dict = {}
    number_of_files = 0
    number_of_directories = 0
    for (root, directories, files) in os.walk(partition):

        number_of_directories += len(directories)
        number_of_files += len(files)

        for file_name in files:

            full_path = os.path.abspath(os.path.join(root, file_name))
            extension = file_name.split(".")[-1]
            extensions.add(extension)

            if extension not in extension_dict.keys():
                extension_dict[extension] = 1
            else:
                extension_dict[extension] += 1

            file_size = os.path.getsize(full_path)
            file_size = convert_size(file_size)
            file_size_dict[file_name] = file_size

    print("Number of directories: {}".format(number_of_directories))
    print("Number of files: {}".format(number_of_files))
    print()

    print("The sorted extensions are: ")
    pprint.pprint(sorted(extensions))
    print()
    print("The dictionary of extensions is: ")
    pprint.pprint(dict(extension_dict))
    print()
    print("The dictionary of files with their sizes is: ")
    pprint.pprint(dict(file_size_dict))


if __name__ == '__main__':
    partition = sys.argv[1]
    partition = partition + ":"
    partition_analysis(partition)
