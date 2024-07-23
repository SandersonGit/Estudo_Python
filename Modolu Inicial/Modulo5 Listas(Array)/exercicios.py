# nomes = ["", "", "", "", ""]
# i = 0

# while i < 5:
#     nome = str(input("Digite um nome"))
#     nomes[i] = nome
#     i = i + 1

# print(nomes)


# aluno = {
#     "Nome": "Sanderson",
#     "idade": 36,
#     "nota": 10
# }

# print(aluno)

# aluno["aprovado"] = True
# del aluno["idade"]

# print(aluno)

# numeros = (5, 10, 15, 20)

# for numero in numeros:
#     print(f"{numero} é o número da tupla numeros")
    
# frutas = ["maçã", "banana", "cereja", "damasco", "figo"]

# del frutas[2]

# print(frutas)

# frutas.append("Kiwi")

# print(frutas)

# carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1964, "cor": "vermelho"}
# print(carro)
# del carro["ano"]
# print(carro)
# carro["preço"] = 40000
# print(carro)

# numeros = [1, 5, 8, 9, 12, 15, 18, 22, 25]

# for numero in numeros:
#     if numero % 2 == 0:
#         print(f"O número {numero} é par!")

# numeros = [3, 5, 7, 9, 11]
# result = 0
# for numero in numeros:
#     result += numero
    
# print(result)    

# numeros = [3, 15, 7, 9, 11]
# result = 0
# for numero in numeros:
#     if numero > result:
#         result = numero

# print(result)

# frutas = ["maçã", "banana", "cereja", "damasco", "figo"]
# print(len(frutas))

produtos = {
    "copo": 5,
    "lancheira": 10,
    "mochila": 15
}

for item in produtos:
    print(f"O preço do {item} é {produtos[item]}")
    
estudante = {
    "nome": "Ana",
    "idade": 32,
    "curso": "Engenharia"
}

for item in estudante:
    if item == "curso":
        print(estudante[item])

cores = ("vermelho", "verde", "azul", "amarelo")

for cor in cores:
    print(f"A cor é {cor}")

animais = ["cachorro", "gato", "coelho", "papagaio", "hamster"]

del animais[2]
animais.append("tartaruga")
print(animais)

nomes = ["Ana", "Bruno", "Carlos", "Diana"]

if "Carlos" in nomes:
    print("Carlos está presente na lista")

carro = {"marca": "Ford", "modelo": "Mustang", "ano": 1964}

carro["ano"] = 2022
carro["cor"] = "Azul"

print(carro)

numeros = [10, 20, 30, 40, 50]
result = 0

for numero in numeros:
    result += numero

print(result)

idades = (15, 20, 25, 30, 35, 40)

for idade in idades:
    if idade >= 25:
        print(idade)
        
nomes = ["Alice", "Bob", "Charlie", "Diana"]

for nome in nomes:
    print(f"O nome {nome}, possui {len(nome)} caracteres!")