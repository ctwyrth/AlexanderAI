import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
  try:
    absolute_base = os.path.abspath(working_directory)
    target_path = os.path.normpath(os.path.join(absolute_base, file_path))

    # guard base folder
    if os.path.commonpath([absolute_base, target_path]) != absolute_base:
      return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # check if file
    if not os.path.isfile(target_path):
      return f'Error: "{file_path}" does not exist or is not a regular file'
    
    # check file extension
    if not target_path.lower().endswith('.py'):
      return f'Error: "{file_path}" is not a Python file'
    
    # building command to run the Python file
    command = ["python", target_path]
    if args != None:
      command.extend(args)

    try:
      finished_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired as te:
      return f'Process timed out after 30 seconds'

    process_output = ""
    if finished_process.returncode != 0:
      process_output = f'Process exited with code "{finished_process}" '
    
    if not finished_process.stdout and not finished_process.stderr:
      process_output += 'No output produced'
    
    if finished_process.stdout:
      process_output += f'STDOUT: {finished_process.stdout} '
    if finished_process.stderr:
      process_output += f'STDERR: {finished_process.stderr}'

    return process_output.strip()

  except Exception as e:
    return f'Error: executing Python file: {e}'
