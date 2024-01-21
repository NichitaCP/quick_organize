import os


def move_file_to_new_folder(old_path, new_path):
    if not os.path.isdir(new_path):
        print(f"Folder {new_path} doesn't exist. Creating new folder")
        os.mkdir(new_path)
    os.rename(old_path, new_path)


def assert_current_directory():
    while True:
        x = input("Do you want to run the script in the current directory? (Where script is located) Y/N \n")
        if x.lower() in ["y", "n"]:
            return x.lower() == 'y'
        else:
            print(f"Please enter Y or N. You entered: {x} \n")


def get_folder_where_to_run_script():
    folder_input = input("Enter the folder name where you want to execute the script... \n")
    return folder_input


def create_all_extensions(directory):
    extensions = list()
    for element in os.listdir(directory):
        full_file_path = os.path.join(directory, element)
        if os.path.isfile(full_file_path):
            name, extension = os.path.splitext(full_file_path)
            if extension not in extensions:
                extensions.append(extension)
    return list(set(extensions))


def main():
    if assert_current_directory():
        cwd = os.getcwd()
        extension_list = create_all_extensions(cwd)
        print(cwd)
        for file in os.listdir(cwd):
            file_path = os.path.join(cwd, file)
            if os.path.isfile(file_path):
                for file_name, file_extension in os.path.splitext(file_path):
                    if file_extension in extension_list:
                        new_folder = file_extension + "_files"
                        new_path = os.path.join(cwd, new_folder)
                        move_file_to_new_folder(cwd, new_path)


if __name__ == "__main__":
    main()













