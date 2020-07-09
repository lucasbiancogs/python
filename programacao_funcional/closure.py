def multiplicar(x):
    '''
    Esse exemplo tem o uso de closure
    que é a capacidade da função de reonhecer suas proximidades
    ela "sabe" onde está inserida
    por isso que podemos colocar multiplicar(2) na variável dobro
    e depois somente chamá-la quantas vezes quiser
    mesmo sem ter a variável y ela sabe q a função mãe a possui

    tem também alta ordem, retornando uma função
    e também de função tardia
    pois tudo só sera resolvido ao inserir o segundo valor
    '''
    def calcular(y):
        return x * y
    return calcular


if __name__ == '__main__':
    print(multiplicar(3)(4))
    dobro = multiplicar(2)
    print(dobro(3))
    print(dobro)
