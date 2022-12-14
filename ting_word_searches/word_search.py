from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    result = []
    for arquivo in instance:
        ocorrencias = [
            {"linha": idx}
            for idx, linha in enumerate(arquivo["linhas_do_arquivo"], start=1)
            if word.lower() in linha.lower()
        ]
        if ocorrencias:
            result.append(
                {
                    "palavra": word,
                    "arquivo": arquivo["nome_do_arquivo"],
                    "ocorrencias": ocorrencias,
                }
            )

    return result


def search_by_word(word: str, instance: Queue):
    """Aqui irá sua implementação"""
