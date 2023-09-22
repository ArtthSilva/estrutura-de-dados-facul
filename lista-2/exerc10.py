class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        aumento = (percentual_aumento / 100) * self.salario
        self.salario += aumento

    def __str__(self):
        return f"Nome: {self.nome}\nSalário: R${self.salario:.2f}\nCargo: {self.cargo}"


funcionario1 = Funcionario("João", 1100, "dev")
print("salario antes do aumento:")
print(funcionario1.salario)

# Aumentar o salário em 10%
funcionario1.aumentar_salario(5)

print("\nsalario após o aumento:")
print(funcionario1.salario)

