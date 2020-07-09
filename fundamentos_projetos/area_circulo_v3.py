from math import pi

'''
Quando se importa somente a funcionalidade
é utilizado a função desejada apenas como uma variável
'''

print('pi = ', pi)
raio = 15.3

area_circulo = pi * raio ** 2
print(f'A área do círculo é: {area_circulo}')

'''
import math

Quando se importa toda a biblioteca
é necessário referenciar a função desejada como um objeto

# print(dir(math))

print('pi = ', math.pi)
raio = 15.3

area_circulo = math.pi * raio ** 2
'''
