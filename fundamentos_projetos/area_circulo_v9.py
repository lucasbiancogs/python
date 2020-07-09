from math import pi


# Função que quando chamada retorna o valor da área
def calcular(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    # É preciso pegar o valor retornado pela função
    area = calcular(raio)
    print('A área do circulo é: %.2f' % area)
