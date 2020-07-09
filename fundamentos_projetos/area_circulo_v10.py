from math import pi
# O import sys pega ações do terminal
import sys


def calcular(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    '''
    O primeiro argumento argv[0] é o nome do arquivo
    O segundo argumento argv[1] é o valor inserido pelo usuário
    logo depois do nome do arquivo
    '''
    raio = sys.argv[1]
    area = calcular(raio)
    print('A área do circulo é: %.2f' % area)
