import os
import json
def main():
    for testfile in os.listdir("tests"):
        if testfile.endswith(".py"):
            os.system(f"python tests/{testfile}")


main()
counter = 0
output = {"output": counter}
with open('output.json', 'w') as json_file:
    json.dump(output, json_file)