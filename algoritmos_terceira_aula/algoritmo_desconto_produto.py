preco_produto = float(input("Informe o preço do produto: ").replace(",","."))

preco_desconto = preco_produto - (preco_produto * 0.10)

print(f"O preço do produto com desconto é de {preco_desconto}")