from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_text = txt_importer(path_file)

    for content in instance._data:
        if path_file in content["file_name"]:
            return None
    file_info = {
        "file_name": path_file,
        "number_of_lines": len(file_text),
        "file_lines": file_text,
    }
    instance.enqueue(file_info)
    # sys.stdout.write(str(file_info))


def remove(instance):
    if instance.is_empty():
        return sys.stdout.write("There is no file to remove\n")

    removed_file = instance.dequeue()
    path_file = removed_file["file_name"]
    sys.stdout.write(f"File {path_file} successfully removed\n")


def file_metadata(instance, position):
    files = instance._data
    if not (-1 < position < len(files)):
        return sys.stderr.write("Invalid position\n")

    file_found = instance.search(position)
    sys.stdout.write(str(file_found))
