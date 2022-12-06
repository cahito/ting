# import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    data = str(instance)
    if path_file in data:
        return print(data)
    lista = txt_importer(path_file)
    linhas = len(lista)
    dicionario = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": linhas,
        "linhas_do_arquivo": lista,
    }
    instance.enqueue(dicionario)
    data = str(instance)
    return print(data)


def remove(instance: Queue):
    if len(instance._data) == 0:
        return print("Não há elementos")
    path_file = instance._data[0]['nome_do_arquivo']
    instance.dequeue()
    return print(f'Arquivo {path_file} removido com sucesso')



def file_metadata(instance: Queue, position: int):
    """Aqui irá sua implementação"""
