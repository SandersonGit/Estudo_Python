# Operadores lógicos

verdadeiro = True
falso = False

print( not verdadeiro)
print( not falso)

print("-------------------------------------------")

a = 5
b = 10
c = 8
d = 8

print(a > b and c > d)
print(a > b and c < d)
print(a < b and c < d)

print(a < b and b > c)

print("-------------------------------------------")


a = 5
b = 10
c = 8
d = 8

print(a > b or c > d)
print(a > b or c < d)
print(a < b or c < d)

print(a < b or b > c)