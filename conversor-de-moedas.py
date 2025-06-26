def conversor_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_dolar = round(valor_reais / taxa_dolar, 2)
    valor_euro = round(valor_reais / taxa_euro, 2)

    print(f"Valor em reais: R$ {valor_reais:.2f}")
    print(f"Valor convertido em dólares: US$ {valor_dolar:.2f}")
    print(f"Valor convertido em euros: € {valor_euro:.2f}")

if __name__ == "__main__":
    valor_em_reais = 100.00
    taxa_dolar = 5.20
    taxa_euro = 6.15

    conversor_moeda(valor_em_reais, taxa_dolar, taxa_euro)
