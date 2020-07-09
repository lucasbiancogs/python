import csv


def read(arq):
    '''
    Para ler o arquivo corretamente é necessário abri-lo com encoding
    o csv.reader já irá pegar as linhas e transformar em arrays (listas)
    '''
    with open(arq, encoding='latin1') as arquivo:
        for dado in csv.reader(arquivo):
            print('{}: {}'.format(dado[8], dado[3]))


def write(arqIn, arqOut):
    with open(arqIn, encoding='latin1') as arquivo:
        '''
        Aqui eu li e escrevi também com encoding
        '''
        with open(arqOut, 'w', encoding='latin1') as arquivo_saida:
            for dado in csv.reader(arquivo):
                print('{}: {}'.format(dado[8], dado[3]),
                      file=arquivo_saida)


def entrada_usuario():
    '''
    Somente uma função para pegar a entrada do usuário
    '''
    entrada = input('Deseja ler (r) ou escrever (w) o arquivo? ')
    if entrada == 'r':
        read('desafio-ibge.csv')
    elif entrada == 'w':
        write('desafio-ibge.csv', 'desafio-ibge.txt')
    else:
        print('É necessário informar r ou w!')
        entrada_usuario()


if __name__ == '__main__':
    entrada_usuario()
