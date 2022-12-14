from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue, com_linha: bool = False):
    result = []
    for arquivo in instance:
        ocorrencias = [
            {"linha": idx, "conteudo": linha}
            for idx, linha in enumerate(arquivo["linhas_do_arquivo"], start=1)
            if word.lower() in linha.lower()
        ]
        if com_linha == False:
            for cada in ocorrencias:
                cada.pop("conteudo")

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
    result = exists_word(word, instance, com_linha=True)

    return result
