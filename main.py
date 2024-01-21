import os


def move_file_to_new_folder(old_path, new_path):
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
            if extension == '.py':
                continue
            elif extension not in extensions:
                extensions.append(extension)
    return list(set(extensions))


def organize_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Specified directory '{directory_path}' does not exist.")
        return

    extension_list = create_all_extensions(directory_path)
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_path)
            if file_extension in extension_list:
                new_folder = os.path.join(directory_path, file_extension + "_files")
                new_path = os.path.join(new_folder, file)
                old_path = file_path

                if not os.path.exists(new_folder):
                    os.mkdir(new_folder)

                move_file_to_new_folder(old_path, new_path)


def main():
    if assert_current_directory():
        organize_files_in_directory(os.getcwd())
    else:
        specified_path = get_folder_where_to_run_script()
        organize_files_in_directory(specified_path)


if __name__ == "__main__":
    main()
