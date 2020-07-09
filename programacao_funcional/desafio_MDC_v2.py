def mdc(numeros):
    '''
    Nessa função ele define a função calc() e a chama para o menor valor

    Nessa função o divisor testa cada um dos números e com o map()
    soma os resultados dos módulos, se forem nulos, é o divisor
    se não, ele tenta com o próximo menor número utilizando recursividade
    '''
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    return calc(min(numeros))


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
