'''
O with: executa um código dado um comando
e com ele é garantido que após o fim do bloco
o que se abriu com ele será fechado
mesmo que não seja feito explicitamente
e mesmo que contenha erros
É muito mais seguro isso que o try: finally:
'''
with open('pessoa.csv') as arquivo:

    for registro in arquivo:
        print('Nome: {}, Idade: {}\n'.format(*registro.strip().split(',')),
              end='')
