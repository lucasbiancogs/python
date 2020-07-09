PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Eu gosto muito de macarrão'
]


for texto in textos:
    '''
    O que aconteceu aqui é que a intersecção serve como um boolean
    Se existe algo, é verdadeiro não precisa fazer mais nada
    Se estiver vazio é falso
    Então se existe ele entra no if
    E depois printa essa intersecção

    Outro detalhe é que deve se usar o set para criar o conjunto
    E o .split() que por padrão vai separar as palavras pelos espaços
    Se não ele irá pegar letra por letra
    '''
    if PALAVRAS_PROIBIDAS.intersection(set(texto.lower()
       .split())):
        print(f'O texto "{texto}" possui '
              'pelo menos uma palavra proibida: ''',
              PALAVRAS_PROIBIDAS.intersection(set(texto.lower()
                                              .split())))
    else:
        print(f'O texto "{texto}" não possui palavras proibidas.')
