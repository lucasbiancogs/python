'''
Isso de abrir o arquivo e o manter aberto
pegando arquivos sob demanda se chama Streaming

Muitas vezes fazer o upload de todo o documento no início
pode ser muito pesado
'''
arquivo = open('pessoas.csv')
for registro in arquivo:
    # Cada registro é uma linha e vem com o \n
    print('Nome: {}, Idade: {}'.format(*registro.split(',')), end='')
# PRECISA FECHAR O ARQUIVO
arquivo.close()
