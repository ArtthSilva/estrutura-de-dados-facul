class Retangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
        print(self.base)
        print(self.altura)

retangulo = Retangulo(5, 10)
print(f'A área do retangulo é: {retangulo.calcular_area()}')