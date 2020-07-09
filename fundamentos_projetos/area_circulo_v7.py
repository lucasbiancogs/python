from math import pi


# Função que quando chamada printa na tela o valor da área
def calcular(raio):
    print('A área do círculo é: ', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    calcular(raio)
