'''
Em python não existem constantes
Então existe a convenção de que variáveis constantes
são definidas com letras maiúsculas
'''
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
    'Eu gosto muito de macarrão'
]

# O primeiro for vai percorrer cada string dentro dos textos
for texto in textos:
    found = False
    '''
    O segundo for vai percorrer cada palavra usando o .split()
    O .split() por padrão separa as palavras dado os espaços
    mas isso pode ser alterado
    '''
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'O texto "{texto}" possui '
                  'pelo menos uma palavra proibida: ''', palavra)
            found = True
            # O break se associa ao bloco mais interno
            break

    if not found:
        print(f'O texto "{texto}" não possui palavras proibidas.')
