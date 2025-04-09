valorConta = float(input("Informe o valor da conta: "))
porcentualGorjeta = float(input("Informe a porcentagem de gorjeta a ser paga: "))

valorGorjeta = (valorConta * porcentualGorjeta) / 100
valorTotal = valorConta + valorGorjeta

print(f"O valor total da conta, incluindo a gorjeta, é de: R$ {valorTotal:.2f}")
