def faixa_etaria(idade):
    # Um jeito de definir um intervalo em python
    if 0 <= idade < 18:
        return 'Menor de idade'
    # Outra forma de definir um intervalo em python
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade > 100:
        return 'Centenário'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    '''
    O for {variável_1} in {variável_2}
    é como um foreach em Java
    ele printa todos valores dentro da variável_2
    o chamando de variável_1
    '''
    for idade in (17, 35, 87, 113, -2):
        print(f'{idade}: {faixa_etaria(idade)}.')
