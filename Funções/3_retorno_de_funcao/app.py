# Define a função saudacao que retorna a mensagem "Olá [nome]!". A função é chamada com "Sanderson", e o resultado é armazenado em sds, que é impresso.

def saudacao(nome):
    return f"Olá {nome}!"

sds = saudacao("Sanderson")

print(sds)

#  Define a função imprimeNome que imprime uma saudação com um nome. O nome é um parâmetro opcional com valor padrão "Matheus". Se nenhum nome for fornecido, a função usa o valor padrão. A função é chamada duas vezes: uma sem argumentos, usando o nome padrão, e outra com o nome "Melanie".

def imprimeNome(nome = "Matheus"):
    print(f"Olá, {nome}!")

imprimeNome()
imprimeNome("Melanie")


# O código define três funções: `soma`, `multiplicacao` e `operacao`. As primeiras realizam operações matemáticas básicas (adição e multiplicação). A função `operacao` aceita duas variáveis e uma função como argumento, aplica a função aos valores e retorna o resultado. O código final chama `operacao` com `soma` e `multiplicacao`, imprimindo os resultados.
# def soma(a, b):
#     return a + b

# def multiplicacao(a , b):
#     return a * b

# def operacao(a, b, f):
#     result = f(a, b)
#     return result

# a = operacao(5, 5, soma)
# print(a)

# b = operacao(10, 5, multiplicacao)
# print(b)

# O código define a função `somaTodos` que aceita um número variável de argumentos (`*nums`). Dentro da função, uma variável `soma` é inicializada em 0 e, em seguida, é incrementada com cada número fornecido. A função retorna a soma total. Exemplos mostram a soma de vários números sendo impressa.
def somaTodos(*nums):
    soma = 0
    for num in nums:
        soma += num
    
    return soma

s = somaTodos(1,5,2,4,44,55,1,123,2,6,9)
print(s)

s2 = somaTodos(1,2,3)
print(s2)


# A função `multiplicaTodos` aceita um número variável de argumentos, itera sobre eles, calcula o produto e retorna o resultado. Os exemplos mostram como a função pode ser usada com diferentes números de argumentos.
def multiplicaTodos(*nums):
    multiplicacao = 1
    for num in nums:
        multiplicacao *= num
    
    return multiplicacao

s1 = multiplicaTodos(2,5,4,6)
print(s1)

s2 = multiplicaTodos(2,5)
print(s2)

# Neste código, usamos funções lambda, que são funções anônimas em Python definidas com a palavra-chave `lambda`. A função `soma` adiciona 10 ao valor de entrada `x`. A função `somaDoiNumeros` soma dois números `a` e `b`. Funções lambda são úteis para definir funções simples de forma concisa.

soma = lambda x: x + 10

print(soma(10))

somaDoiNumeros = lambda a, b: a + b

print(somaDoiNumeros(10, 10))