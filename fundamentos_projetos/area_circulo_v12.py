from math import pi
import sys


def calcular(raio):
    return pi * float(raio) ** 2


# Criando uma função sem entrada e sem saída para o help
def help():
    print(f"""\
É necessário informar o raio do círculo
Sintaxe: python {sys.argv[0]} <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = calcular(raio)
        print('A área do circulo é: %.2f' % area)
