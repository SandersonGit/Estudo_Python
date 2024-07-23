lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista)

i = 0

while i < len(lista):
    if lista[i] % 2 != 0:
        del lista[i]
    
    i += 1

print(lista)