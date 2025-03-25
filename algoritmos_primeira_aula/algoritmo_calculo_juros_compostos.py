#solicita os capital inicial ao usuário
capital_inicial = float(input("Informe o capital inicial: "))
#solicita a taxa de juros ao usuário
taxa_juros = float(input("Informe a taxa de juros (% ao mês): "))
#solicita o tempo ao usuário
tempo_meses = int(input("Informe o tempo em meses: "))

#calcula o montante final
montante_final = capital_inicial * ((1 + (taxa_juros / 100)) ** tempo_meses)

#exibe os valores do cálculo para o usuário
print("------------- Exibição do Montante Final -------------")
#exibe o montante final ao usuário
print(f"O montante final é R$ {montante_final:.2f}")
