def print_file_data(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The file could not be found. Please verify the file path.")

def copy_file_contents(src_path, dest_path):
    try:
        with open(src_path, 'r') as src_file:
            content = src_file.read()
        
        with open(dest_path, 'w') as dest_file:
            dest_file.write(content)
        
        print(f"File successfully copied from {src_path} to {dest_path}")
    except FileNotFoundError:
        print("Source file is missing. Please check the file path.")
    except Exception as error:
        print(f"An issue occurred: {error}")

def modify_file(file_path, new_content):
    try:
        print("Previous file content:")
        with open(file_path, 'r') as file:
            print(file.read())
        
        with open(file_path, 'w') as file:
            file.write(new_content)
        print("The file content has been updated.")
        
        print("Current file content:")
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("The file could not be found. Please verify the file path.")
    except Exception as error:
        print(f"An issue occurred: {error}")

if __name__ == "__main__":
    file_path = "example_file8.txt"
    copy_target = "example_copy.txt"
    updated_content = "This is the updated content for the file."

    print("------ Display File Data -----")
    print_file_data(file_path)

    print("\n----- Copy File Contents -----")
    copy_file_contents(file_path, copy_target)

    print("\n----- Modify and Display File Content -----")
    modify_file(file_path, updated_content)
