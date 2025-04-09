n1 = int(input("Informe o número 1: "))
sinal = input("Qual conta você deseja fazer? (+,-,/,*): ")
n2 = int(input("Informe o número 2: "))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

if sinal == "+":
    print(f"{n1}{sinal}{n2}={adicao}")
elif sinal == "-":
    print(f"{n1}{sinal}{n2}={subtracao}")
elif sinal == "*":
    print(f"{n1}{sinal}{n2}={multiplicacao}")
else:
    print(f"{n1}{sinal}{n2}={divisao}")
