'''
Isso de abrir o arquivo e o manter aberto
pegando arquivos sob demanda se chama Streaming

Muitas vezes fazer o upload de todo o documento no início
pode ser muito pesado
'''
arquivo = open('pessoas.csv')
for registro in arquivo:
    '''
    O .strip() tira os caractéres do início e do fim da string
    e por padrão tira os espaços
    '''
    print('Nome: {}, Idade: {}\n'.format(*registro.strip().split(',')), end='')
arquivo.close()
