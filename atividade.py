
quantidade = int(input("Digite a quantidade de itens: "))

total = 0

for i in range(1, quantidade + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total += preco

media = total / quantidade

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")

valor = 1200.00

print("=" * 35)
print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor:.2f}")
print("=" * 35)

for parcelas in range(1, 11):
    valor_parcela = valor / parcelas
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")

print("=" * 35)

consumo_total = 0
dias_acima = 0

for dia in range(1, 8):
    consumo = float(input(f"Consumo do dia {dia} (kWh): "))
    consumo_total += consumo

    if consumo > 20:
        dias_acima += 1

print("\nResultado da semana")
print(f"Consumo total: {consumo_total:.2f} kWh")
print(f"Dias acima de 20 kWh: {dias_acima}")

for i in range(15, -1, -1):
    print(i)

print("Servidor desligado com segurança.")
