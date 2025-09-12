import os
import config

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(full_path):
        return (f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        with open(full_path, "r") as f:
            f.read()
    except Exception as e:
        return f'Error: {e}'

    with open(full_path, "r") as f:
        file_content = f.read(config.max)
        file_check = f.read()
        if len(file_check) > config.max:
            file_content += (f'[...File "{file_path}" truncated at 10000 characters]')

    return file_content
