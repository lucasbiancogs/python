from random import randint

# laço infinito
'''
while True:
    print('Vai demorar muitooooooo')
'''


def ConfereValores(num1, num2):
    '''
    Essa função cria frases que ridicularizam o usuário
    quando utiliza o mesmo número repetidamente
    '''
    frases_de_alerta = ['Sério mesmo cara?',
                        'Nah, não pode ser que tu tentou com o mesmo número.',
                        'Tu não entendeu nada né',
                        'Tu é tansa']
    if num1 == num2:
        print(frases_de_alerta[randint(0, len(frases_de_alerta) - 1)])


# O número informado é -1 para entrar no laço while
numero_informado = -1
numero_secreto = randint(0, 100)
# Mostra a resposta para sair mais rápido do programa
print(numero_secreto)

# Verifica se o número secreto coincide com o número informado
while numero_informado != numero_secreto:
    numero_antigo = numero_informado
    numero_informado = int(input('Informe o número: '))
    ConfereValores(numero_antigo, numero_informado)

# Caso os números coincidam ele sai do laço e avisa isso na tela
print(f'O número secretro {numero_secreto} foi encontrado!')
