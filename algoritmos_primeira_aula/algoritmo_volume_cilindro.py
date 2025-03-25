#importa a biblioteca de matemática do python, assim é possível utilizar o pi
import math

#pergunta ao usuário o raio
raio = r = int(input("Informe o raio do cilindro: "))
#pergunta ao usuário a altura
altura = h = int(input("Informe a altura do cilindro: "))

#calcula a área da base do cilindro
area_base_cilindro = A = math.pi*r**2
#calcula o volume do cilindro
volume_cilindro = V = A*h

#exibe os valores do cálculo para o usuário
print("-------------Exibindo área da base e volume-------------")
#exibe os valores do cálculo da área da base para o usuário, o ":.2f" serve para exibir apenas duas casas decimais após a virgula do número
print(f"A área da base do cilindro é {A:.2f}")
#exibe os valores do cálculo da altura para o usuário
print(f"A altura do cilindro é {V:.2f}")