
# Este código demonstra como criar e acessar elementos de uma tupla em Python. Também ilustra que tuplas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação. Tentativas de modificar uma tupla resultam em um erro.
tupla = (1, 2, 3)

print(tupla)
print(type(tupla))

# tupla[0] = 5

print(tupla[0])

for x in tupla:
    print(x)