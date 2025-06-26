def calcular_desconto(nome_produto, preco_original, percentual_desconto):
    valor_desconto = round(preco_original * (percentual_desconto / 100), 2)
    preco_final = round(preco_original - valor_desconto, 2)

    print(f"Produto: {nome_produto}")
    print(f"Preço original: R$ {preco_original:.2f}")
    print(f"Desconto: {percentual_desconto}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    nome_produto = "Camiseta"
    preco_original = 50.00
    percentual_desconto = 20

    calcular_desconto(nome_produto, preco_original, percentual_desconto)
