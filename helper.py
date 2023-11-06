import os

# Set the directory you want to start from
rootDir = 'response_form_clean'  # Replace with the path to the directory you want to process

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Scanning directory: %s' % dirName)
    for fname in fileList:
        if fname.lower().endswith('.txt'):
            # Full path of .txt file
            txt_file_path = os.path.join(dirName, fname)
            # New file name with .py extension
            py_file_path = os.path.join(dirName, fname[:-4] + '.py')

            print('Converting "%s" to "%s"...' % (txt_file_path, py_file_path))

            # Reading the content of .txt file and writing it to .py file
            with open(txt_file_path, 'r') as txt_file, open(py_file_path, 'w') as py_file:
                py_file.write(txt_file.read())

            # Delete the original .txt file
            os.remove(txt_file_path)
            print('Deleted "%s"' % txt_file_path)

print('Conversion and cleanup complete.')