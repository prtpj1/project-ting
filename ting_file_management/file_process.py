from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_text = txt_importer(path_file)

    for content in instance._data:
        if path_file in content["nome_do_arquivo"]:
            return None
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_text),
        "linhas_do_arquivo": file_text,
    }
    instance.enqueue(file_info)
    sys.stdout.write(str(file_info))


def remove(instance):
    ...


def file_metadata(instance, position):
    ...
