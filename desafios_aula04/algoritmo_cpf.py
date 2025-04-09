pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

print("------------ Descobrir os dígitos verificadores do CPF -----------")

while True:
    CPF = []
    digitos = input("Informe os 9 primeiros dígitos do seu CPF: ")

    if not digitos.isdigit() or len(digitos) != 9:
        print("Entrada inválida. Digite apenas 9 números.")
        continue

    for i in range(9):
        CPF.append(int(digitos[i]))

    soma1 = sum(CPF[i] * pesos1[i] for i in range(9))
    digito1 = 11 - (soma1 % 11)
    if digito1 >= 10:
        digito1 = 0
    CPF.append(digito1)

    soma2 = sum(CPF[i] * pesos2[i] for i in range(10))
    digito2 = 11 - (soma2 % 11)
    if digito2 >= 10:
        digito2 = 0
    CPF.append(digito2)

    print("------------Exibição-----------")
    print(f"O seu CPF é {CPF[0]}{CPF[1]}{CPF[2]}.{CPF[3]}{CPF[4]}{CPF[5]}.{CPF[6]}{CPF[7]}{CPF[8]}-{CPF[9]}{CPF[10]}")
    print(f"Os dígitos verificadores são: {CPF[9]} e {CPF[10]}")

    novamente = input("Deseja consultar o dígito verificador de outro CPF? (s/n): ").strip().lower()
    
    if novamente != "s":
        print("Programa encerrado.")
        break  

lista = []
def adicionar_nome(): 
    lista.append(nome)
    return llista

nome = input("digite seu nome")
