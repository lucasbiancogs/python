from math import pi

'''
Quando um script é importado ele é automaticamente lido
Isso nem sempre é desejado
Quando se roda um arquivo diretamente pelo terminal
ele se torna o arquivo principal e é chamado de '__main__'
Todos arquivos que depois são importados
Recebem o seu próprio nome
Por isso neste código se verifica
Se for o script principal ele irá se chamar '__main__'
E então irá rodar o bloco
Se ele for importado, ele não roda
'''

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    print('A área do círculo é: ', pi * float(raio) ** 2)
