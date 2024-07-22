# Este código define um dicionário `carro` com características do carro, como número de portas, janelas, motor, teto solar e câmbio. O `print(carro)` exibe todo o dicionário. O `print(carro["portas"])` acessa e imprime o valor associado à chave `"portas"`, que é `4`. O `print(carro["cambio"])` acessa e imprime o valor associado à chave `"cambio"`, que é `"Automático"`. Isso demonstra como criar e acessar dados em um dicionário Python.

carro = {
    "portas": 4,
    "janelas": 4,
    "motor": 2.0,
    "teto_solar": True,
    "cambio": "Automático"
}

print(carro)

print(carro["portas"])
print(carro["cambio"])

# Este código define um dicionário `livros` onde as chaves são títulos de livros e os valores são quantidades ou preços associados a esses livros. O `print(livros)` exibe todo o dicionário. Neste exemplo, as chaves são `"harry_pother"`, `"Senhor_dos_aneis"`, e `"Piercy_Jackson"`, com valores `1000`, `2000`, e `1000` respectivamente. Isso demonstra como criar e exibir um dicionário em Python.

livros = {
    "harry_pother": 1000,
    "Senhor_dos_aneis": 2000,
    "Piercy_Jackson": 1000
}

print(livros)

# O código percorre cada livro no dicionário livros, imprimindo o nome do livro e a quantidade de páginas associadas a ele.

for livro in livros:
    print(livro)
    print(f"O livro {livro} tem {livros[livro]} páginas")

# O código verifica a existência de chaves em um dicionário e imprime os valores associados às chaves encontradas.

pessoa = {
    "nome": "Sanderson",
    "idade": 36
}

print(pessoa)
print("nome" in pessoa)
print("sobrenome" in pessoa)

if "nome" in pessoa:
    print(f"Seu nome é {pessoa['nome']}")
if "sobrenome" in pessoa:
    print(f"Seu sobrenome é {pessoa['sobrenome']}")
    
# Este código demonstra como criar um dicionário vazio, adicionar elementos a ele, e remover elementos usando a palavra-chave del. É uma forma básica de manipulação de dicionários em Python.
dic = {}
print(dic)

dic["nome"] = "Sanderson"
dic["idade"] = "36"

print(dic)

del dic["nome"]

print(dic)

# Este código demonstra como criar um dicionário com informações, adicionar novos elementos a ele e remover elementos usando a palavra-chave del. Essas operações são fundamentais para manipular dicionários em Python.
carro = {
    "pneus": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4
}

print(carro)

carro["teto solar"] = 1

print(carro)

del carro["motor"]
del carro["janelas"]

print(carro)
