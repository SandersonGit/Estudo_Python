# lista = [0, 1, 2, 3, 4]
# print(lista)

# lista.append(5)

# print(lista)

# lista.append(6)

# print(lista)

# lista = []

# print(lista)

# i = 0

# while i < 5:
#     elemento = input("Digite um nome")
#     lista.append(elemento)
#     i += 1
    
# print(lista)

frutas = ["Maçã", "Uva", "Cajú"]
verduras = ["Alface", "Couve", "Agrião"]
juntos = []

i = 0
while i < len(frutas):
    juntos.append(frutas[i])
    i += 1

i = 0
while i < len(verduras):
    juntos.append(verduras[i])
    i += 1

print(juntos)
