lado1 = int(input("Informe o primeiro valor: "))
lado2 = int(input("Informe o segundo valor: "))
lado3 = int(input("Informe o terceiro valor: "))

print("--------------- Classificação dos Triângulos ---------------")

if lado1 == lado2 and lado1 == lado3:
    print(f"O seu triângulo é equilátero, pois todos os lados são iguais lado 1: {lado1}, 2: {lado2}, 3: {lado3}") 
elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado1 == lado3 and lado1 != lado2:
    print(f"O seu triângulo é isóceles, pois dois lados são iguais e um é diferente, lado 1: {lado1}, 2: {lado2}, 3: {lado3}")
else:
    print(f"O seu triângulo é escaleno, pois todos os lados são diferentes,lado 1: {lado1}, 2: {lado2}, 3: {lado3}")
