import os

directory = r"C:\Users\Nichita\Downloads"

for element in os.listdir(directory):
    element_file_path = os.path.join(directory, element)
    file_name, file_extension = os.path.splitext(element_file_path)
    print(file_name, file_extension)