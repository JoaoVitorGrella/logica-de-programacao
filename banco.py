acervo = [
    {"codigo": 301, "titulo": "Camiseta", "autor": "Nike", "paginas": 300, "disponivel": True},
    {"codigo": 302, "titulo": "Calca Jeans", "autor": "Levis", "paginas": 200, "disponivel": False},
    {"codigo": 303, "titulo": "Jaqueta", "autor": "Adidas", "paginas": 350, "disponivel": True},
    {"codigo": 304, "titulo": "Tenis", "autor": "Puma", "paginas": 280, "disponivel": True}
]

novo_livro = {
    "codigo": 305,
    "titulo": "Moletom",
    "autor": "Adidas",
    "paginas": 320,
    "disponivel": True
}

acervo.append(novo_livro)

print("Produtos disponíveis na loja:")

for livro in acervo:
    if livro["disponivel"] == True and livro["paginas"] > 250:
        print("Produto:", livro["titulo"])
        print("Marca:", livro["autor"])
        print("------------------------")

encontrado = False

for livro in acervo:
    if livro["codigo"] == 304:
        encontrado = True
        print("\nProduto encontrado!")
        print("Nome:", livro["titulo"])

        if livro["disponivel"] == True:
            print("Situação: Disponível")
        else:
            print("Situação: Esgotado")

        break

if encontrado == False:
    print("Código 304 não encontrado.")

codigo = int(input("\nDigite o código do produto que deseja comprar: "))

encontrado = False

for livro in acervo:
    if livro["codigo"] == codigo:
        encontrado = True

        if livro["disponivel"] == True:
            livro["disponivel"] = False
            print("Compra realizada com sucesso!")
            print("Produto comprado:", livro["titulo"])
        else:
            print("Esse produto está fora de estoque.")

        break

if encontrado == False:
    print("Produto não encontrado.")

print("\nEstoque atualizado:")

for livro in acervo:
    print(livro)
