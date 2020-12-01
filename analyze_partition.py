import math
import os
import pprint
import sys

import matplotlib.pyplot as plt
import numpy as np


# def create_pie_chart(extension_dict):
#     keys = extension_dict.keys()
#     values = extension_dict.values()
#
#     fig1, ax1 = plt.subplots()
#     ax1.pie(values, labels=keys, autopct='%1.1f%%', startangle=90)
#     ax1.axis('equal')
#
#     # Show graphic
#     plt.show()
#
#
# def create_bar_chart(dictionary_of_dir_files):
#     keys = dictionary_of_dir_files.keys()
#     values = dictionary_of_dir_files.values()
#
#     y_pos = np.arange(len(values))
#     plt.bar(y_pos, values)
#     plt.xticks(y_pos, keys)
#
#     plt.show()

def create_charts(dictionary_of_dir_files, extension_dict, converted_file_sizes):
    # Pie chart
    keys = dictionary_of_dir_files.keys()
    values = dictionary_of_dir_files.values()

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=keys, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    # Pie chart
    keys = extension_dict.keys()
    values = extension_dict.values()

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=keys, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')


    # Barchart
    # keys = converted_file_sizes.keys()
    # values = converted_file_sizes.values()
    # converted_values = list(values)
    # for i in range(len(converted_values)):
    #     new_value = convert_size(converted_values[i])
    #     converted_values[i] = new_value
    #
    # y_pos = np.arange(len(converted_values))
    # plt.bar(y_pos, converted_values)
    # plt.xticks(y_pos, keys)

    # Show graphic
    plt.show()


def convert_size(size_in_bytes):
    if size_in_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    power = math.pow(1024, i)
    result = round(size_in_bytes / power, 2)
    return "%.2f %s" % (result, size_name[i])


def partition_analysis(partition):
    dictionary_of_dir_files = {}
    extensions = set()
    extension_dict = {}
    file_size_dict = {}
    number_of_files = 0
    number_of_directories = 0
    converted_file_sizes = {}

    for (root, directories, files) in os.walk(partition):

        number_of_directories += len(directories)
        number_of_files += len(files)
        dictionary_of_dir_files = {'directories': number_of_directories, 'files': number_of_files}

        for file_name in files:

            full_path = os.path.abspath(os.path.join(root, file_name))
            extension = file_name.split(".")[-1]
            extensions.add(extension)

            if extension not in extension_dict.keys():
                extension_dict[extension] = 1
            else:
                extension_dict[extension] += 1

            file_size = os.path.getsize(full_path)
            # file_size = convert_size(file_size)
            if extension not in file_size_dict.keys():
                file_size_dict[extension] = file_size
            else:
                file_size_dict[extension] += file_size

            # converted_file_sizes ={}
            # for key, value in file_size_dict.items():
            #     value = convert_size(float(value))
            #     converted_file_sizes[key] = value

            # file_size_dict[file_name] = file_size

    print("Number of directories: {}".format(number_of_directories))
    print("Number of files: {}".format(number_of_files))
    print()

    print("The sorted extensions are: ")
    pprint.pprint(sorted(extensions))
    print()
    print("The dictionary of extensions is: ")
    pprint.pprint(extension_dict)
    print()
    print("The dictionary of files with their sizes is: ")
    pprint.pprint(file_size_dict)

    create_charts(dictionary_of_dir_files, extension_dict, file_size_dict)


if __name__ == '__main__':
    partition = sys.argv[1]
    partition = partition + ":"
    partition_analysis(partition)
