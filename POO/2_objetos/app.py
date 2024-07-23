# Este código define a classe `Pessoa` com um construtor `__init__` que inicializa três atributos: `nome`, `idade` e `profissao`. Em seguida, cria uma instância da classe chamada `matheus`, passando "Matheus", 29 e "Programador" como argumentos. O código imprime a instância `matheus`, seu tipo, e os valores dos atributos `nome`, `idade` e `profissao`. Também atribui o valor do atributo `nome` a uma variável `nome` e imprime esse valor. O método `print(matheus)` mostra o objeto como uma representação padrão, que pode ser menos informativa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

matheus = Pessoa("Matheus", 29, "Programador")

print(matheus)
print(type(matheus))
print(matheus.nome)
print(matheus.idade)
print(matheus.profissao)

nome = matheus.nome
print(nome)


# O código define a classe Carro, que tem um construtor __init__ para inicializar cinco atributos: portas, motor, tetoSolar, marca e preco.

# Em seguida, cria duas instâncias da classe: ferrari e lamborguine, com diferentes valores para cada atributo. O código imprime os valores dos atributos para cada carro, mostrando informações como marca, motor, número de portas, preço e se possui teto solar.

class Carro:
    def __init__(self, portas, motor, tetoSolar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.tetoSolar = tetoSolar
        self.marca = marca
        self.preco = preco

ferrari = Carro(2, 4.0, True, "Ferrari", 100.000 )
lamborguine = Carro(4, 3.0, False, "Lamborguine", 200.000)

print(ferrari.marca, ferrari.motor, ferrari.portas, ferrari.preco, ferrari.tetoSolar)
print(lamborguine.marca, lamborguine.motor, lamborguine.portas, lamborguine.preco, lamborguine.tetoSolar)