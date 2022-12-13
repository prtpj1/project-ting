def exists_word(word, instance):
    existent_word = list()
    occurrences = list()
    data = instance._data[0]

    for pos, line in enumerate(data["linhas_do_arquivo"]):
        if word.casefold() in line.casefold():
            occurrences.append({"linha": pos + 1})

    if len(occurrences) > 0:
        existent_word.append(
            {
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
        )

    return existent_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
