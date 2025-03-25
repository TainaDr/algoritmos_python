capital_inicial = float(input("Informe o capital inicial: ").replace(",","."))
taxa_juros = float(input("Informe a taxa de juros: "))
tempo = int(input("Informe o tempo (em meses): "))

taxa_juros = taxa_juros/100
montante = capital_inicial + (capital_inicial*taxa_juros*tempo)

print(f"O montante final é: R${montante}")