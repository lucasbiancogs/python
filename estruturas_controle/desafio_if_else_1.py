import sys
import errno


class TerminalColor:
    ERRO = '\033[1;31m'
    DEF = '\033[0;0m'


def help():
    print(TerminalColor.ERRO +
          'Nota inválida, insira notas no intervalo de 0 à 10.' +
          TerminalColor.DEF)


def media_aluno_in():
    media_aluno = input('Insira a média do aluno: ')
    return float(media_aluno)


def conceito(nota):
    if nota > 10.0 or nota < 0.0:
        help()
        sys.exit(errno.EINVAL)
    elif nota >= 9:
        return 'A'
    elif nota >= 8:
        return 'A-'
    elif nota >= 7:
        return 'B'
    elif nota >= 6:
        return 'B-'
    elif nota >= 5:
        return 'C'
    elif nota >= 4:
        return 'C-'
    elif nota >= 3:
        return 'D'
    elif nota >= 2:
        return 'D-'
    elif nota >= 1:
        return 'E'
    else:
        return 'E-'


if __name__ == '__main__':
    media_aluno = media_aluno_in()
    print('O aluno teve média %.1f e conceito %s.' %
          (media_aluno, conceito(media_aluno)))
