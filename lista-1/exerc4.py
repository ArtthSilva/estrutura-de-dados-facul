numeros = []

n = int(input("Quantos números você deseja inserir? "))

for i in range(n):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

if numeros:
    maior = max(numeros)
    menor = min(numeros)

    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("A lista está vazia.")
