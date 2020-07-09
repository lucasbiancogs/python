# Implementação simplificada do map
def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)


if __name__ == '__main__':
    '''
    O map não calcula tudo de uma vez ele te devolve um generator
    que pode ser usado como quiser

    No caso de definir list, ele já percorre todos na lista
    '''
    print(list(mapear(lambda x: x ** 2, [2, 3, 4])))
