import os
from collections import defaultdict


def get_extensions(partition):
    extensions = set()
    extension_dict = {}
    for (root, directories, files) in os.walk(partition):
        for file_name in files:
            full_path = os.path.abspath(os.path.join(root, file_name))
            extension = file_name.split(".")[-1]
            extensions.add(extension)
            file_length = os.path.getsize(full_path)
            if extension not in extension_dict.keys():
                extension_dict[extension] = [1, file_length]
            else:
                extension_dict[extension] = [int(extension_dict.get(extension)) + 1, file_length]

    print("The sorted extensions are: {}".format(sorted(extensions)))
    print("The dictionary of extensions is: {}".format(str(dict(extension_dict))))


get_extensions("F:")


# def get_extensions(partition):
#     extensions = set()
#     extension_dict = defaultdict(int)
#     for (root, directories, files) in os.walk(partition):
#         for file_name in files:
#             extension = file_name.split(".")[-1]
#             extensions.add(extension)
#             # file_length = os.path.getsize(file_name)
#             # info_list = [extension_dict[extension] + 1, file_length]
#             extension_dict[extension] += 1
#
#     print("The sorted extensions are: {}".format(sorted(extensions)))
#     print("The dictionary of extensions is: {}".format(str(dict(extension_dict))))
#
#
# get_extensions("F:")
