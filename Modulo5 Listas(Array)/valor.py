# Este código encontra o maior valor em uma lista de números. Ele percorre cada elemento da lista e, se o elemento atual for maior que maiorValor, atualiza maiorValor com o valor desse elemento. Ao final do loop, maiorValor contém o maior número da lista, que é então impresso.

lista = [13, 555, 87, 12, 5, 137, 422]

maiorValor = 0

for n in lista:
    if n > maiorValor:
        maiorValor = n

print(maiorValor)

# Este código encontra o menor valor em uma lista de números. Inicialmente, `menorValor` é definido como 1000. O loop percorre cada elemento da lista e, se o elemento atual for menor que `menorValor`, atualiza `menorValor` com o valor desse elemento. Ao final do loop, `menorValor` contém o menor número da lista, que é então impresso.

menorValor = 1000

for i in lista:
    if i < menorValor:
        menorValor = i

print(menorValor)