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

def soma(a, b):
    return a + b

def multiplicacao(a , b):
    return a * b

def operacao(a, b, f):
    result = f(a, b)
    return result

a = operacao(5, 5, soma)
print(a)

b = operacao(10, 5, multiplicacao)
print(b)