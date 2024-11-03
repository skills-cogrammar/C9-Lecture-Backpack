import traceback


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file path '{file_path}' was not found!")
    except Exception as e:
        print(f"An exception error occurred:")
        traceback.print_exc()


read_file("not_found.csv")
