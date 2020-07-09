def divisores(num):
    '''
    Essa função pega um número e retorna seus divisores sob demanda
    '''
    return (divisor for divisor in range(1, num + 1) if num % divisor == 0)


def divisor_comum(numeros):
    '''
    Essa função pega a lista de números, define o menor
    pega sua lista de divisores e o retira.

    Então, para cada número da lista de divisores
    ele verifica se o número esta presente
    na lista de valores do número subsequente
    se sim, ele o adiciona a lista de divisores comuns
    '''
    divisor_comum = []
    numeros_ordenados = sorted(numeros)
    menores_divisores = divisores(min(numeros))
    numeros_ordenados.pop(0)
    for numero in numeros_ordenados:
        for divisor in menores_divisores:
            if divisor in divisores(numero):
                divisor_comum.append(divisor)
    return divisor_comum


def mdc(numeros):
    return max(divisor_comum(numeros))


if __name__ == '__main__':
    '''
    O objetivo aqui é encontrar o maior divisor comum
    Os resultados são:
    No 01 => 7
    No 02 => 5
    No 03 => 3
    No 04 => 11
    No 05 => 15
    No 06 => 1
    '''

    print(mdc([21, 7]))

    print(mdc([125, 40]))

    print(mdc([9, 564, 66, 3]))

    print(mdc([55, 22]))

    print(mdc([15, 150]))

    print(mdc([7, 9]))
