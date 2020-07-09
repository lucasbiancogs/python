PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Eu gosto muito de macarrão'
]


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'O texto "{texto}" possui '
                  'pelo menos uma palavra proibida: ''', palavra)
            break
    else:
        print(f'O texto "{texto}" não possui palavras proibidas.')
