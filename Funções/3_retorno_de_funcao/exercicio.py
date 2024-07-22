# Define a função maiorQ para verificar se num é maior ou menor que 10 e retornar uma mensagem. O usuário insere um número, que é passado para a função. A mensagem resultante é impressa.


def caracteres(texto):
    if len(texto) > 20:
        return "Esse texto é muito longo!"
    else:
        return "Texto de tamanho perfeito!"

texto1 = input("insira um texto")

print(caracteres(texto1))

# Define a função retornaPar que recebe uma lista l e retorna uma nova lista contendo apenas os números pares. Ela itera sobre cada número em l, verifica se é par usando numero % 2 == 0, e adiciona à nova lista se for o caso. A função é aplicada a duas listas diferentes, e os resultados são impressos.

def retornaPar(l):
    novaLista = []
    
    for numero in l:
        if numero % 2 == 0:
            novaLista.append(numero)
        
    return novaLista

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaPar = retornaPar(lista)

print(listaPar)   

lista2 = [125, 256, 48, 8963, 325, 45, 10, 587]

print(retornaPar(lista2))


# Define a função calculamedia que calcula a média dos valores em uma lista l. A função acumula a soma dos elementos e divide pelo número de elementos da lista. Em seguida, retorna o resultado. A função é aplicada a duas listas diferentes, e as médias calculadas são impressas.

def calculamedia(l):
    soma = 0
    
    for i in l:
        soma += i
    
    resultado = soma / len(l)
    return resultado

lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [125, 256, 48, 8963, 325, 45, 10, 587]

print(calculamedia(lista1))
print(calculamedia(lista2))

    
    