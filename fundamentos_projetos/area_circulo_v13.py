from math import pi
import sys
'''
O import errno, é uma biblioteca de erros padrão do sistema
'''
# import errno


def calcular(raio):
    return pi * float(raio) ** 2


def help():
    print(f"""\
É necessário informar o raio do círculo
Sintaxe: python {sys.argv[0]} <raio>""")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        '''
        Aqui se sairia do programa ao verificar o erro com o .exit
        a entrada escolhida (errno.EPERM) identifica que o programa teve erro
        sendo um programa rodado normamente = 0
        e um programa com erro, no caso do EPERM, = 1
        que quer dizer que a operação não foi permitida
        '''
        # sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = calcular(raio)
        print('A área do circulo é: %.2f' % area)
