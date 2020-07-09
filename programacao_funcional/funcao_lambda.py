compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14}
)

'''
A função map() mapeia cada componente do item dado como parâmetro
no caso do exemplo -> compras
e faz uma ação para cada um, dada a função inserida

O lambda é uma função anônima que necessariamente irá dar algum retorno
ela define a entrada e indica o retorno
lamda entrada: retorno
'''
totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preco'],
        compras
    )
)

print(f'Preços totais: {totais}')
print(f'Total: {sum(totais)}')
