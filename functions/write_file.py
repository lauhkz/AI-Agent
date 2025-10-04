import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    current_file = os.path.abspath(os.path.join(working_directory, file_path))
    try:
        if not current_file.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        current_file = current_file.split("/")
        file = current_file.pop()
        current_file = "/".join(current_file)
        if not os.path.exists(current_file):
            os.makedirs(current_file)

        with open(os.path.abspath(os.path.join(current_file, file)), "w") as f:
            result = f.write(str(content))
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error reading file "{current_file}": {e}'


