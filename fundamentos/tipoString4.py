a = '123'
b = ' de Oliveira 4'
c = a + b
print(c)
c = a.__add__(b)
print(c)
c = str.__add__(a, b)
print(c)
