# Aqui está a explicação detalhada do código:
# A classe `Carro` possui:
# - Um construtor `__init__` que inicializa os atributos `marca`, `valor`, `portas` e `combustivel`.
class Carro:
    def __init__(self, marca, valor, portas, combustivel):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.combustivel = combustivel
    
    # - O método `abastecer()`, que define o atributo `combustivel` como 100.
    # - O método `dirigir()`, que diminui o atributo `combustivel` em 10 a cada chamada.
    def abastecer(self):
        self.combustivel = 100
    
    def dirigir(self):
        self.combustivel -= 10


# O código cria uma instância `fusca` com os atributos definidos. O estado do carro é impresso após cada operação de dirigir e, finalmente, após abastecer. O consumo de combustível é demonstrado com múltiplas chamadas ao método `dirigir()`, e o abastecimento é mostrado com a chamada ao método `abastecer()`.
fusca = Carro("Volks-Wagem", 50.000, 2, 100)
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)


fusca.dirigir()
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)
fusca.dirigir()
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)
fusca.dirigir()
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)
fusca.dirigir()
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)
fusca.dirigir()
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)

fusca.abastecer() 
print(fusca.marca, fusca.valor, fusca.portas, fusca.combustivel)

# Um construtor __init__ que inicializa os atributos usuario e saldo.
class Conta:
    def __init__(self, usuario, saldo):
        self.usuario = usuario
        self.saldo = saldo
    
    #O método saque(valor), que reduz o saldo pelo valor especificado.
    def saque(self, valor):
        self.saldo -= valor

    #O método deposito(valor), que aumenta o saldo pelo valor especificado.
    def deposito(self, valor):
        self.saldo += valor 
    
# O código cria uma instância sanderson com saldo inicial de 100. 
sanderson = Conta("Sanderson", 100)
print(sanderson.usuario, sanderson.saldo)

# Após um saque de 50 e um depósito de 200, o saldo é atualizado e impresso após cada operação.
sanderson.saque(50)
print(sanderson.usuario, sanderson.saldo)

sanderson.deposito(200)
print(sanderson.usuario, sanderson.saldo)
           