class Aluno:
    def __init__(self):
        self.nome = ""
        self.nota = 0.0

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def set_nota(self, nota):
        self.nota = nota

    def get_nota(self):
        return self.nota

if __name__ == "__main__":
    aluno = Aluno()
    soma = 0.0
    print("Informe o nome:")
    nome = input()
    aluno.set_nome(nome)

    print("Quantas notas?")
    qnt_notas = int(input())

    for i in range(1, qnt_notas + 1):
        print(f"Nota {i}:")
        notas = float(input())
        aluno.set_nota(notas)
        soma += aluno.get_nota()

    result = soma / qnt_notas
    if result >= 7:
        print("Aprovado")
    elif result < 4:
        print("Reprovado")
    else:
        print("Final")

    print(f"Média: {result}\nAluno: {aluno.get_nome()}")
