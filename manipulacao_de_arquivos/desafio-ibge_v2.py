import csv
from urllib import request
'''
Esse request de urllib  vai baixar o arquivo para ler
'''


def read_url(url, ent):
    '''
    Com request.urlopen() ao invés de abrir um arquivo local
    É aberto um arquivo no navegador
    '''
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1')
        print('Download concluído.')
        if ent == 'r':
            read(dados)
        else:
            write(dados, 'desafio-ibge.txt')


def read(arq):
    for cidade in csv.reader(arq.splitlines()):
        print(f'{cidade[8]}: {cidade[3]}')


def write(arq, arqOut):
    with open(arqOut, 'w', encoding='latin1') as arquivo_saida:
        for cidade in csv.reader(arq.splitlines()):
            print('{}: {}'.format(cidade[8], cidade[3]),
                  file=arquivo_saida)


def entrada_usuario():
    entrada = input('Deseja ler (r) ou escrever (w) o arquivo? ')
    if entrada == 'r' or 'w':
        # É utilizado o r para ele ler a url crua
        read_url(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv',
                 entrada)
    else:
        print('É necessário informar r ou w!')
        entrada_usuario()
    nova_acao()


def nova_acao():
    entrada = input('Deseja fazer algo mais (s/n)? ')
    if entrada == 's':
        entrada_usuario()
    elif entrada == 'n':
        pass
    else:
        print('É necessário informar s ou n!')
        nova_acao()


if __name__ == '__main__':
    entrada_usuario()
