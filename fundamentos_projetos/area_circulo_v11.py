from math import pi
import sys


def calcular(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    # Essa validação é variável com o arquivo utilizado
    if len(sys.argv) < 2:
        print(f"""\
É necessário informar o raio do círculo
Sintaxe: python {sys.argv[0]} <raio>""")

    else:
        raio = sys.argv[1]
        area = calcular(raio)
        print('A área do circulo é: %.2f' % area)
