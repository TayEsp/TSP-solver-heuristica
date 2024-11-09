import platform
from math import sqrt

def os_path_converter(path: str) -> str:
    """
        funcao para converter padrao de diretorios entre linux e windows
    """
    if platform.system().lower() == "linux":
        path = path.replace("\\", "/")
    else:
        path = path.replace("/", "\\")

    return path


def remove_emptys_list_and_casting(list_check: list, cast="") -> list:
    """
        Funcao para remover itens considerados vazios em uma lista: espacos apenas, quebras de linha,
        None, string vazia. Tambem faz troca de tipo de todos os dados.

        cast: FLOAT, INT, STRING

    """
    list_checked = []
    for item in list_check:
        item = item.strip()

        if item is not None and  item != "" and item != "\n":
            if cast == "":
                list_checked.append(item)
            elif cast == "STRING":
                list_checked.append(str(item))
            elif cast == "FLOAT":
                list_checked.append(float(item))
            elif cast == "INT":
                list_checked.append(int(item))

    return list_checked

def node_distance(x1, y1, x2, y2):
    a = (x2 - x1) ** 2
    b = (y2 - y1) ** 2
    return sqrt(a + b)
