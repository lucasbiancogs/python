'''
for i in range(1, 10):
    if i == 6:
        break
    print(i, end=(' '))
# O else não é executado se ele encontrar o break
else:
    print('Fim')
'''
from random import randint


def numero_da_sorte():
    # Retorna um inteiro de 1 a 6
    return randint(1, 6)


print('Início')
for numero in range(1, 7):
    # Se for impar ele continua
    if numero % 2 == 1:
        continue
    # Se for par e igual ao número da sorte ele para
    elif numero % 2 == 0 and numero == numero_da_sorte():
        print('ACERTOU!', numero)
        break
else:
    print('Não acertou')
print('Fim')
