class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'meu nome é {self.nome}')

pessoa = Pessoa('arthur', 19)
pessoa.falar()