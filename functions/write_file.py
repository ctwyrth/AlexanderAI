import os

def write_file(working_directory: str, file_path:str, content: str) -> str:
  try:
    absolute_base = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(absolute_base, file_path))

    if os.path.commonpath([absolute_base, target_path]) != absolute_base:
      return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_path):
      return f'Error: Cannot write to "{file_path}" as it is a directory'

    parent_directory = os.path.dirname(target_path)
    os.makedirs(parent_directory, exist_ok=True)

    with open(target_path, 'w', encoding="UTF-8") as f_dest:
      f_dest.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

  except Exception as e:
    return f'Error: {str(e)}'
