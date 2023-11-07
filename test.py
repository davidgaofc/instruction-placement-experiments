import os
import json
from glob import glob

def main():
    for testfile in os.listdir("tests"):
        if testfile.endswith(".py"):
            os.system(f"python tests/{testfile}")


main()
counter = 0
directory = 'results'  # Replace with your directory path
json_pattern = os.path.join(directory, '*.json')

# Initialize totals
total_pre = 0
total_post = 0
total_intra = 0

# Iterate over JSON files in the directory
for json_file_path in glob(json_pattern):
    try:
        with open(json_file_path, 'r') as json_file:
            # Load data from JSON file
            data = json.load(json_file)

            # Sum scores from each category
            total_pre += sum(data.get('pre', []))
            total_post += sum(data.get('post', []))
            total_intra += sum(data.get('intra', []))
    except (IOError, ValueError) as e:
        print(f"Error reading {json_file_path}: {e}")

# Print the total scores
print(f"Total 'pre' scores: {total_pre}")
print(f"Total 'post' scores: {total_post}")
print(f"Total 'intra' scores: {total_intra}")
counter = total_pre + total_post + total_intra
output = {"output": 100*(counter/600), "pre": 100*(total_pre/200), "post": 100*(total_post/200), "intra": 100*(total_intra/200)}

with open('output.json', 'w') as json_file:
    json.dump(output, json_file)