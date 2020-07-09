def main():
    from pessoas import Pessoa, Vendedor, Cliente
    from loja.compras import Compra

    print('Inicio do programa.')
    lucas = Pessoa('Lucas', 23)
    print(lucas)

    joao = Vendedor(nome='João pé de feijão', idade=22, salario=2800)
    print(joao)

    nairana = Cliente('Nairana', 19)
    print(nairana)

    tenis = Compra('Tênis Nike', joao, 340, 2020, 4, 10)
    print(tenis)

    nairana += tenis
    nairana += Compra('Calça legging', joao, 109)
    nairana += Compra('Casaco de lã', joao, 112)
    print(f'O total das compras foi de: {nairana.total_compras()}')
    print(f'A última compra foi \
no dia: {nairana.get_data_ultima_compra()}')

    nairana += Compra('Sutiã', joao, 60, 2020, 4, 17)
    print(f'O total das compras foi de: {nairana.total_compras()}')
    print(f'A última compra foi \
no dia: {nairana.get_data_ultima_compra()}')

    nairana += Compra('Casaco de veludo', joao, 80, 2020, 4, 10)
    print(f'O total das compras foi de: {nairana.total_compras()}')
    print(f'A última compra foi \
no dia: {nairana.get_data_ultima_compra()}')


if __name__ == '__main__':
    main()
