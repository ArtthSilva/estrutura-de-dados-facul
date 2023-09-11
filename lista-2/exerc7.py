class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f'marca do carro: {self.marca} \nmodelo: {self.modelo} \nano: {self.ano}')

carro1 = Carro('Chevrolet ', 'Celta', 2000)
carro1.detalhes()