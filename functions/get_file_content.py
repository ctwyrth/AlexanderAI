# pull file content if valid file path is provided, otherwise return error message
import os

def get_file_content(working_directory: str, file_path: str) -> str:
  try:
    absolute_base = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(absolute_base, file_path))

    if not os.path.isfile(target_path):
      return f'Error: File not found or is not a regular file: "{file_path}"'

    if os.path.commonpath([absolute_base, target_path]) != absolute_base:
      return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'

    # print(f"Reading file: {target_path}")

    MAX_CHARS = 10000
    with open(target_path, "r", encoding="utf-8") as f_source:
      raw_content = f_source.read(MAX_CHARS + 1)
    
      # Check if there are more characters to read
    if len(raw_content) > MAX_CHARS:
      content = raw_content[:MAX_CHARS] + f'[...File "{target_path}" truncated at {MAX_CHARS} characters]'
    else:
      content = raw_content

    # dest_path = os.path.normpath(os.path.join(absolute_base, "destination.txt"))
    # with open(dest_path, 'w', encoding="utf-8") as f_dest:
    #   f_dest.write(content)

    return content
  except Exception as e:
    return f'Error: {str(e)}'