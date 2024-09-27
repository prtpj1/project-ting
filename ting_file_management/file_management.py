import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                content = file.read()
                new_content = content.split("\n")
                return new_content
        except FileNotFoundError:
            return sys.stderr.write(f"File {path_file} not found\n")

    return sys.stderr.write("Invalid file\n")
