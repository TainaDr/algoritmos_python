# #Desafio
# # Crie um gerador que receba os 8 primeiros dígitos e calcule qual deve ser o dígito verificador correto.Em vez de validar um RG, você deverá criar um gerador que receba os 8 primeiros dígitos e calcule qual deve ser o dígito verificador correto.

pesos = [3, 2, 7, 6, 5, 4, 3, 2]

print("------------ Descobrir dígito verificador de RG no estado do Paraná-PR -----------")

while True:
    rg = []
    digitos = input("Informe os 8 primeiros dígitos do seu rg: ")

    if not digitos.isdigit() or len(digitos) != 8:
        print("Entrada inválida. Digite apenas 8 números.")
        continue

    for i in range(8):
        rg.append(int(digitos[i]))

    multiplicacao = (rg[i] * pesos [i] for i in range(8))
    soma = sum(multiplicacao)
    modulo = soma % 11
    digito_verificador = 11 - modulo

    if digito_verificador >= 10:
        digito_verificador = 0

    print("------------Exibição-----------")
    print(f"O seu RG é {rg[0]}{rg[1]}.{rg[2]}{rg[3]}{rg[4]}.{rg[5]}{rg[6]}{rg[7]}-{digito_verificador}")
    print(f"O dígito verificador é: {digito_verificador}")

    novamente = input("Deseja consultar o dígito verificador de outro RG? (s/n): ").strip().lower()
    
    if novamente != "s":
        print("Programa encerrado.")
        break  
