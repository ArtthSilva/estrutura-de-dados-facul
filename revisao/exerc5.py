contador = 0
soma = 0
lista = [4,6,5,]
for numero in lista:
    if (numero % 2) == 0:
        soma += numero
        contador += 1

result = soma / contador
print(result)