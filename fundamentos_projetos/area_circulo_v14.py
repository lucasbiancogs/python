from math import pi
import sys
import errno


def calcular(raio):
    return pi * float(raio) ** 2


def help():
    print(f"""\
É necessário informar o raio do círculo
Sintaxe: python {sys.argv[0]} <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    # Essa validação é para caso o valor inserido não seja numérico
    if not sys.argv[1].isnumeric():
        help()
        print('O raio deve ser um valor numérico')
        # Esse erro quer dizer que a entrada foi inválida = 2
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = calcular(raio)
    print('A área do circulo é: %.2f' % area)
