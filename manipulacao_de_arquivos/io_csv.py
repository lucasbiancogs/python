import csv

with open('pessoas.csv') as entrada:
    '''
    o csv.reader já separa o arquivo por linhas e vírgulas
    o que facilita muito
    '''
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
