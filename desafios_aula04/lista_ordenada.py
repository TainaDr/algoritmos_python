quantidadeProdutos = int(input("Quantos produtos você deseja informar? "))
soma = 0
listaProdutos = []

for i in range (1,quantidadeProdutos + 1):
    produto = input(f"Informe o nome do produto {i}:")
    listaProdutos.append(produto)
    listaProdutos.sort()

print("-------- Lista de produtos em ordem alfabética --------")
print(listaProdutos)


