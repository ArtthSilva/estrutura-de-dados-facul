def terceiro_maior(vetor):
    valores_unicos = set(vetor)
    
    if len(valores_unicos) < 3:
        return "Não há terceiro maior valor."
    
    valores_ordenados = sorted(valores_unicos, reverse=True)
    
    return valores_ordenados[2]

vetor = [5, 2, 7, 5, 2, 8, 1, 9, 7]
resultado = terceiro_maior(vetor)
print("O terceiro maior valor é:", resultado)
