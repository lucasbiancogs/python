from math import pi
import sys
import errno


'''
Criando uma classe para organizar melhor
Isso irá ser visto em outros capítulos
'''


class TerminalColor:
    '''
    Esses códigos de cores são encontrados na internet
    ERRO -> Vermelho
    NORMAL -> Cor padrão
    '''
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


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

    if not sys.argv[1].isnumeric():
        help()
        '''
        Deixando essa linha em vermelho
        É necessário inserir a cor e depois retirar a cor
        Caso contrário irá sempre manter a cor inserida
        '''
        print(TerminalColor.ERRO +
              'O raio deve ser um valor numérico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = calcular(raio)
    print('A área do circulo é: %.2f' % area)
