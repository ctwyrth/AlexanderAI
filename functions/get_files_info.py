import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
  try:
    absolute_base = os.path.abspath(working_directory)
    directory_path = os.path.normpath(os.path.join(absolute_base, directory))
    file_info = []

    if directory == ".":
      file_info.append("Result for current directory:")
    else:
      file_info.append(f"Result for '{directory}' directory:")

    if not os.path.isdir(directory_path):
      file_info.append(f'   Error: "{directory}" is not a directory')
      return "\n".join(file_info)

    if os.path.commonpath([absolute_base, directory_path]) != absolute_base:
      file_info.append(f'   Error: Cannot list "{directory}" as it is outside the permitted working directory')
      return "\n".join(file_info)

    contents = os.listdir(directory_path)

    for item in contents:
      item_path = os.path.join(directory_path, item)
      if os.path.isfile(item_path):
        size = os.path.getsize(item_path)
        file_info.append(f" - {item}: file_size={size} bytes, is_dir=False")
      elif os.path.isdir(item_path):
        size = os.path.getsize(item_path)
        file_info.append(f" - {item}: file_size={size} bytes, is_dir=True")
    
    constructed_info = "\n".join(file_info)
    
    if not file_info:
      return f'Success: "{directory}" is a valid directory within the working directory, but it is empty'
    return constructed_info
  except Exception as e:
    return f'Error: {str(e)}'
  
