produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}
print("===== CADASTRO DO PRODUTO =====")
print("Dicionário completo:", produto)

print("Nome do produto:", produto["nome"])
print("Preço do produto: R$", produto["preco"])

produto["preco"] = 220.0
produto["estoque"] += 6
produto["categoria"] = "Periféricos"

print("===== PRODUTO ATUALIZADO =====")
print(produto)

usuario = {
    "nome": "joao vitor",
    "nivel": "Administrador",
    "ativo": True
}

print("===== PERFIL DO USUÁRIO =====")

print("Dados do usuário:", usuario)

print("Chaves cadastradas:")
print(usuario.keys())

print("Valores cadastrados:")
print(usuario.values())

print("===== FIM DO PROGRAMA =====")
