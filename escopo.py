def soma_ate(n):
    # Caso base
    if n == 1:
        return 1

    # Passo recursivo
    else:
        return n + soma_ate(n - 1)


# Teste do programa
resultado = soma_ate(5)

print(f"A soma acumulada é: {resultado}")
