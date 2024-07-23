# Neste código, a classe `Carro` é definida com um construtor `__init__` para inicializar os atributos `marca` e `preco`. 
class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco
    
    # A classe possui dois métodos:
    # - `ligar()`: Imprime "Vrummmmmmmmm", simulando o som do carro ao ser ligado.
    # - `mudarPreco(novoPreco)`: Atualiza o atributo `preco` com um novo valor fornecido.
    def ligar(self):
        print("Vrummmmmmmmm")
    
    def mudarPreco(self, novoPreco):
        self.preco = novoPreco
        

# O código cria uma instância `polo` com marca "VW" e preço inicial de 60.000. Após ligar o carro, o preço é alterado para 90.000, e ambos os valores são impressos.      
polo = Carro("VW", 60000)
print(polo.marca, polo.preco)
polo.ligar()
polo.mudarPreco(90000)
print(polo.marca, polo.preco)




