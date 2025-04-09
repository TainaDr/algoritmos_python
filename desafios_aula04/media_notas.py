# nota1 = float(input("Informe a nota 1: "))
# nota2 = float(input("Informe a no2ta 2: "))
# nota3 = float(input("Informe a nota 3: "))
# nota4 = float(input("Informe a nota 4: "))

# mediaNotas = (nota1 + nota2 + nota3 + nota4) / 4

# print("Sua média é:", mediaNotas)

# if mediaNotas < 5: 
#     print("Você foi reprovado :(")
# elif mediaNotas >= 5 and mediaNotas < 7:
#     print("Você está de recuperação ;(")
# else:
#     print("Você foi aprovado ;)")2

#UTILIZANDO FOR:

soma = 0
quantidadeNotas = int(input("Quantas notas você deseja informar? "))

for i in range (1,quantidadeNotas + 1):
    nota = float(input(f"Informe a nota {i}:"))
    soma += nota

mediaNotas = soma / quantidadeNotas

if mediaNotas < 5: 
    print(f"Sua média é {mediaNotas:.2f} Infelizmente, você foi reprovado :(")
elif mediaNotas >= 5 and mediaNotas < 7:
    print(f"Sua média é {mediaNotas:.2f} Você está de recuperação ;(")
else:
    print(f"Sua média é {mediaNotas:.2f} Parabéns, você foi aprovado ;)")
