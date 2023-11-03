import os
def main():
    for testfile in os.listdir("tests"):
        if testfile.endswith(".py"):
            os.system(f"python tests/{testfile}")

main()