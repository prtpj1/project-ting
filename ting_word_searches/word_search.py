import json
from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    existent_word = list()
    occurrences = list()
    data = instance._data[0]

    for pos, line in enumerate(data["file_lines"]):
        if word.casefold() in line.casefold():
            occurrences.append({"line": pos + 1})

    if len(occurrences) > 0:
        existent_word.append(
            {
                "word": word,
                "file": data["file_name"],
                "occurrences": occurrences,
            }
        )

    return existent_word


if __name__ == "__main__":
    word = input("Type the word to be searched: ")
    file_path = input("Type the file path where the word will be searched: ")

    queue_instance = Queue()
    process(file_path, queue_instance)
    result = exists_word(word, queue_instance)

    print(json.dumps(result, indent=2))


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
