def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    
    tamanho = len(vetor_ordenado)
    indice_do_meio = tamanho // 2
    valor_mediana = vetor_ordenado[indice_do_meio]
    
    return valor_mediana

vetor = [5, 2, 7, 8, 1]
resultado = mediana(vetor)
print("A mediana é:", resultado)
