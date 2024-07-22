# O código define três listas de jogadores (`flamengo`, `corinthians`, `vasco`) e as agrupa na lista `times`. O `print(times)` exibe todas as listas de jogadores. O `print(times[0])` acessa e exibe a lista de jogadores do `flamengo`. O `print(times[0][1])` acessa o segundo jogador da lista `flamengo` e imprime "Guilherme". Isso mostra como acessar elementos em listas aninhadas.

flamengo = ["Ronaldo", "Guilherme", "Marcelo"]
corinthians = ["Charles", "Sampaio", "Arthur"]
vasco = ["Ratinho", "Cabeça", "Marcos"]

times = [flamengo, corinthians, vasco]

print(times)

print(times[0])

print(times[0][1])

# Este código define três listas (`copo`, `lancheira`, `mochila`), cada uma contendo informações sobre um item (nome, cor, preço). Essas listas são agrupadas na lista `kitEscola`. O `print(kitEscola[0])` exibe a lista `copo`. O `print(kitEscola[1])` exibe a lista `lancheira`. O `print(kitEscola[2])` exibe a lista `mochila`. Isso demonstra como armazenar e acessar múltiplas listas dentro de uma lista maior.

copo = ["Artes Copos", "Preto", 50]
lancheira = ["ASmérica", "Azul", 35]
mochila = ["Andaluzia", "Branco", 100]

kitEscola = [copo, lancheira, mochila]

print(kitEscola[0])
print(kitEscola[1])
print(kitEscola[2])
    