'''
Para evitar que o arquivo tenha problemas e nunca chegue no comando
arquivo.close()
podemos usar o try: - finally:
ele irá tentar rodar o código abaixo e se não conseguir
mesmo assim irá rodar o finally
O bloco do try: pode ser considerado como "arriscado"

Vale ressaltar que qualquer coisa fora do finally não será executado
caso haja um erro
Então se o bloco após try contenha um erro
as linhas 33 e 34 não serão executadas
'''
try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}\n'.format(*registro.strip().split(',')),
              end='')
# except IndexError:
#     pass
finally:
    print('teste')
    arquivo.close()
'''
O except verifica o erro encontrado em try: e caso encontre o tipo
executa o código, no caso pass é um código em branco
o que significa que ele irá seguir após o finally
'''

if arquivo.closed:
    print('O arquivo já foi fechado.')
