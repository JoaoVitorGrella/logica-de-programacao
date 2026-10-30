valores = [ 12, 45, 7, 89, 23]
indice_menor = 0
indice_maior = 0

for i in range(1, len(valores)):
    if valores[i] < valores[indice_menor]:
        indice_menor = i
    if valores[i] > valores[indice_maior]:
        indice_maior = i
        
