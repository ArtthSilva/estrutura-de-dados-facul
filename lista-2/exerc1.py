class Circulo:

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14 * (self.raio ** 2)
        return area

circulo = Circulo(5)
print(f'A area do circulo é: {circulo.calcular_area()} cm²')