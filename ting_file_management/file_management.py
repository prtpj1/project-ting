import sys


def txt_importer(path_file):
    if path_file.endswith(".txt"):
        try:
            with open(path_file, "r") as file:
                content = file.read()
                new_content = content.split("\n")
                return new_content
        except FileNotFoundError:
            return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    return sys.stderr.write("Formato inválido\n")
