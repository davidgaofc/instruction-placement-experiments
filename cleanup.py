import os
import glob

def delete_py_files_recursively(directory_path):
    # Walk through the directory
    for root, dirs, files in os.walk(directory_path):
        # Find all .py files in current directory
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"Deleting {file_path}")
                os.remove(file_path)  # Delete the file

delete_py_files_recursively("responses")