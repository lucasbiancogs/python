print(True or False)
print(7 != 3)
print(2 > 3)
print(7 != 3 and 2 > 3)
print('')

# Tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True and True and True and True)
print(True and True and True and False)
print('')

# Tabela verdade do OU
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('')

# Tabela verdade do XOR
print(True != True)
print(True != False)
print(False != True)
print(False != False)
print(True != False != False != False != False != False)
print('')

# Operador de negação (unário)
print(not True)
print(not False)
print(not 0)
print(not 1)
print(not not 1)
print(not not True)
print('')

# Cuidado com operadores bit-a-bit!
print(True & True)
print(True | True)
print(True ^ False)
print('')

'''
3 -> 11
2 -> 10
3 & 2
Eles operam bit por bit, pode ficar meio imprevisível
_ -> 10
_ -> 2

3 | 2
_ -> 11
_ -> 3
'''

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = (salario - despesas) >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
