peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

altura
imc = peso/altura ** 2

print("----------- Calculadora de IMC - índice de massa corporal -----------")

if (imc < 18.5 ):
    print(f"O seu IMC é de {imc:.2f}. Você está abaixo do peso :(.")
elif (18.5 <= imc < 25):
    print(f"O seu IMC é de {imc:.2f}.Você está com o peso normal ;).")
elif (25 <= imc < 25):
    print(f"O seu IMC é de {imc:.2f}.Cuidado, você está em sobrepeso.")
else:
    print(f"O seu IMC é de {imc:.2f}.Você está com obesidade :/.")
