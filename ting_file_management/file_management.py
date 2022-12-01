import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, encoding="utf-8") as file:
            arquivo = file.read()
            lista_arquivo = arquivo.split("\n")
            return lista_arquivo
    except Exception:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
