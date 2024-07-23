class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca
    
    def ligar(self):
        print("Vrummmmmmm")
        
class Carro(Veiculo):
    def __init__(self, rodas, marca, tetoSolar):
        super().__init__(rodas, marca)
        self.tetoSolar = tetoSolar

ferrari = Carro(4, "Ferrari", True)

print(ferrari.marca)