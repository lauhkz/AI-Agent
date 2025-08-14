import os

def get_files_info(working_directory, directory=""):
    dirs = os.listdir(os.path.abspath(working_directory))
    if directory == ".":
        dirs = os.listdir(working_directory)
    if directory not in dirs and directory != ".":
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        result = "Result for current directory:"
        current = os.path.abspath(working_directory)
        print(f"path: {os.path.abspath(working_directory)}")
        print(f"dirs: {dirs}")
        #print("Result for current directory:")
        for file in dirs:
            abs_file = os.path.join(current, file)
            size = os.path.getsize(abs_file)
            is_dir = os.path.isdir(abs_file)
            print(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
            result += f"\n- {file}: file_size={size} bytes, is_dir={is_dir}"
        return result
            
