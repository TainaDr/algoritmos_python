peso = float(input("Informe o seu peso(kg): "))
altura = float(input("Informe a sua altura(m): "))

altura
imc = peso/altura ** 2

print("----------- Calculadora de IMC - índice de massa corporal -----------")
print(f"O seu imc é de {imc:.2f}")
