import os

def list_of_file_in_directory(path_directory):
    try:
        list_files = os.listdir(path_directory)
        return list_files
    except FileNotFoundError:
        return []

directory = "C:\Games"
files = list_of_file_in_directory(directory)
if files:
    print("List of files in the directory:")
    for item in files:
        print(item)
else:
    print("The directory was not found or is empty.")
