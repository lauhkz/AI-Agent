import os
from google.genai import types

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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write the content provided to a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File were to write the content provided, has to be in to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="content to be written in the file",
            ),
        },
        required=[ "content", "file_path"],
    ),
)
