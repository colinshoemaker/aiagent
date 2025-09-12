import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(full_path):
        return (f'Error: "{directory}" is not a directory')

    try:
        path = os.listdir(full_path)
    except Exception as e:
        return f"Error: {e}"

    l_content = []

    for file in path:
        item_path = os.path.join(full_path, file)

        try:
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
        except Exception as e:
            return f"Error: {e}"

        l_content.append(f"- {file}: file_size={size} bytes, is_dir={is_dir}")
    content = "\n".join(l_content)
    return content
