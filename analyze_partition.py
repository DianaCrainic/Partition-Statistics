import math
import os
import pprint
import sys

from cutecharts.charts import Bar
from cutecharts.charts import Pie
from cutecharts.components import Page


def create_chart_dir_files(dictionary_of_dir_files):
    labels = list(dictionary_of_dir_files.keys())
    values = list(dictionary_of_dir_files.values())
    chart = Pie("The chart for the number of directories and files")
    chart.set_options(labels=labels, inner_radius=0)
    chart.add_series(values)
    return chart


def create_chart_extension_dict(extension_dict):
    labels = list(extension_dict.keys())
    values = list(extension_dict.values())
    chart = Pie("The chart for the number of file extensions")
    chart.set_options(labels=labels, inner_radius=0)
    chart.add_series(values)
    return chart


def create_chart_file_size_dict(file_size_dict):
    labels = list(file_size_dict.keys())
    values = list(file_size_dict.values())
    chart = Bar("Bar chart")
    chart.set_options(labels=labels, x_label="Extensions", y_label="counter")
    chart.add_series("The number", values)
    return chart


def number_of_elements(number_of_directories, directories, number_of_files, files):
    number_of_directories += len(directories)
    number_of_files += len(files)
    return number_of_directories, number_of_files


def print_number_of_elements(dictionary_of_dir_files):
    print("Number of directories: {}".format(list(dictionary_of_dir_files.values())[0]))
    print("Number of files: {}".format(list(dictionary_of_dir_files.values())[1]))
    print()


def get_extensions(extension, extensions, extension_dict):
    extensions.add(extension)
    if extension not in extension_dict.keys():
        extension_dict[extension] = 1
    else:
        extension_dict[extension] += 1

    return extensions, extension_dict


def print_extensions_info(extensions, extension_dict):
    print("The sorted extensions are: ")
    pprint.pprint(sorted(extensions))
    print()
    print("The dictionary of extensions is: ")
    pprint.pprint(extension_dict)
    print()


def get_file_sizes(full_path, extension, file_size_dict):
    file_size = os.path.getsize(full_path)
    if extension not in file_size_dict.keys():
        print("Extension {}, file_size {}".format(extension, file_size))
        file_size_dict[extension] = file_size
    else:
        print("Extension {}, file_size {}".format(extension, file_size))
        file_size_dict[extension] += file_size
    return file_size_dict


def print_file_sizes_info(file_size_dict):
    print("The dictionary of files with their sizes is: ")
    pprint.pprint(file_size_dict)


def convert_size(size_in_bytes):
    if size_in_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_in_bytes, 1024)))
    power = math.pow(1024, i)
    result = round(size_in_bytes / power, 2)
    return "%.2f %s" % (result, size_name[i])


def partition_analysis(partition_name):
    dictionary_of_dir_files = {}
    extensions = set()
    extension_dict = {}
    file_size_dict = {}
    number_of_files = 0
    number_of_directories = 0

    for (root, directories, files) in os.walk(partition_name):

        number_of_directories, number_of_files = number_of_elements(number_of_directories, directories, number_of_files,
                                                                    files)
        dictionary_of_dir_files = {'directories': number_of_directories, 'files': number_of_files}

        for file_name in files:
            extension = file_name.split(".")[-1]
            extensions, extension_dict = get_extensions(extension, extensions, extension_dict)

            full_path = os.path.abspath(os.path.join(root, file_name))
            file_size_dict = get_file_sizes(full_path, extension, file_size_dict)

    print_number_of_elements(dictionary_of_dir_files)
    print_extensions_info(extensions, extension_dict)
    print_file_sizes_info(file_size_dict)

    page = Page()
    page.add(create_chart_dir_files(dictionary_of_dir_files), create_chart_extension_dict(extension_dict),
             create_chart_file_size_dict(file_size_dict))
    page.render()


if __name__ == '__main__':
    partition = sys.argv[1]
    partition = partition + ":"
    partition_analysis(partition)
