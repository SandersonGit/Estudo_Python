# O código define a classe `Pessoa` em Python. A classe possui um método especial chamado `__init__`, que é o construtor da classe. Este método é chamado automaticamente quando uma nova instância da classe é criada. O construtor recebe três parâmetros: `nome`, `idade` e `sobrenome`, e os usa para inicializar os atributos da instância. `self` refere-se à própria instância da classe e é usado para armazenar os valores fornecidos nos atributos `nome`, `idade` e `sobrenome` para cada objeto da classe `Pessoa`.

class Pessoa:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome