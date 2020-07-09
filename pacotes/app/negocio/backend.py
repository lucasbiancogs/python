nomes = []


def add_nome(nome):
    nomes.append(nome)
    return nomes


def nome_existe(nome):
    if nome in nomes:
        return True
    else:
        return False
