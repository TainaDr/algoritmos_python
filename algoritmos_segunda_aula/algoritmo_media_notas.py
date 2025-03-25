nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira segunda nota: "))

media = (nota1 + nota2)/2

print("--------------- Calculadora de média final ---------------")

if (media >= 7):
    print(f"A sua média foi {media}. Parabéns, você foi aprovado!")
elif (5 <= media < 7):
    print(f"A sua média foi {media}. Você está de recuperação!")
else:
    print(f"A sua média foi {media}.Que pena, você foi reprovado!")

#Forma alternativa:
# soma = 0
# quantidadeNotas = int(input("Quantas notas você deseja informar? "))

# for i in range (1,quantidadeNotas + 1):
#     nota = float(input(f"Informe a nota {i}:"))
#     soma += nota

# mediaNotas = soma / quantidadeNotas

# if mediaNotas < 5: 
#     print(f"Sua média é {mediaNotas:.2f} Infelizmente, você foi reprovado :(")
# elif mediaNotas >= 5 and mediaNotas < 7:
#     print(f"Sua média é {mediaNotas:.2f} Você está de recuperação ;(")
# else:
#     print(f"Sua média é {mediaNotas:.2f} Parabéns, você foi aprovado ;)")