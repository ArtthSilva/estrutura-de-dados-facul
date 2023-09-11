class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        valor = self.preco * self.quantidade
        return print(f'o produto: {self.nome} custa R${valor}')

produto = Produto('crack', 15, 3)
produto.calcular_total()