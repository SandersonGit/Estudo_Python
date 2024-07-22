# Este código usa um loop for para iterar sobre uma sequência de números de 0 a 9 gerada pela função range(10). Em cada iteração, o valor de x é impresso. Se x for igual a 5, o código imprime "Aconteceu alguma coisa".

for x in range(10):
    print(x)
    if x == 5:
        print("Aconteceu alguma coisa")

# Este código usa um loop for para iterar sobre uma sequência de números gerada pela função range(). O range(0, 20, 2) cria uma sequência de números de 0 a 19, com um passo de 2. Em cada iteração, x assume um valor dessa sequência e o print(x) exibe esse valor.

for x in range(0, 20, 2):
    print(x)

# Este código utiliza um loop `for` para iterar sobre uma sequência de números gerada pela função `range()`. O `range(3, 100, 3)` cria uma sequência de números começando em 3, indo até 99 (exclusive), com incrementos de 3. Em cada iteração, o valor de `x` é impresso.

for x in range(3, 100, 3):
    print(x)

