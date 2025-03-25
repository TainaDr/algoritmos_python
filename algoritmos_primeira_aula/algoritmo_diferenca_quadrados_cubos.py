#pergunta ao usuário o primeiro número
n1 = x = int(input("Informe o primeiro número inteiro: "))
#pergunta ao usuário o segundo número
n2 = y = int(input("Informe o segundo número inteiro: "))

#calcula a diferença entre os quadrados
diferenca_quadrados = D = (x**2) - (y**3)

#calcula o módulo
if (D < 0):
    D *= -1

#exibe os valores do cálculo para o usuário
print("--Exibição da diferença entre o quadrado do primeiro número e o cubo do segundo número--")
#exibe os valores do cálculo da difernça entre os quadrados e cubos para o usuário
print(f"A diferença entre quadrados e cubos é {diferenca_quadrados}")
#exibe os valores do cálculo do módulo para o usuário
print(f"O módulo é {D}")
