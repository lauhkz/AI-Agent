import os

def get_files_info(working_directory, directory=""):
    dirs = check_and_set_dir(working_directory, directory)
    #print(dirs)
    result = f"Result for '{directory}' directory:"
    if directory == ".":
        result = f"Result for current directory:"
    for file in os.listdir(dirs):
        if file.startswith((".", "_")):
            continue
        else:
            current_file = os.path.abspath(os.path.join(dirs, file))
            size = os.path.getsize(current_file)
            is_dir = os.path.isdir(current_file)
            result += f"\n- {file}: file_size={size} bytes, is_dir={is_dir}"
    result += f'\nError: '
    print(result)
    return result



def check_and_set_dir(base_dir, directory):
    local_dirs = os.listdir(base_dir) 
    if directory == ".":
        return os.path.abspath(base_dir)
    if directory not in local_dirs:
        raise Exception( f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    base = os.path.join(base_dir, directory)
    if not os.path.isdir(base):
        raise Exception(f'Error: "{directory}" is not a directory')
    else:
        return os.path.abspath(base)


