lista = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 72, 81, 89, 94, 99]

numero = int(input("Digite o número que deseja buscar: "))

inicio = 0
fim = len(lista) - 1
comparacoes = 0
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    comparacoes += 1

    if lista[meio] == numero:
        posicao = meio
        break

    elif numero > lista[meio]:
        inicio = meio + 1

    else:
        fim = meio - 1

if posicao != -1:
    print(f"Número {numero} encontrado no índice {posicao}.")
else:
    print(f"Número {numero} não foi encontrado na lista.")

print(f"Total de comparações realizadas: {comparacoes}")
