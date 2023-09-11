class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        print(f'Titulo do livro: {self.titulo} \nautor: {self.autor}')


livro = Livro('O mito de Sísifo', 'Eu')
livro.detalhes()