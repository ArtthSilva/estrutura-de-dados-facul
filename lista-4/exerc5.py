def remove_duplicatas(vetor):
    vetor_alteracao = []
    for elemento in vetor:
        if elemento not in vetor_alteracao:
            vetor_alteracao.append(elemento)
    return vetor_alteracao

vetor=[1,1,2,4,7,2]
print(vetor)
print(remove_duplicatas(vetor))