valor_reais = float(input("Informe um valor em reais que deseja converter - BRL: ").replace(",","."))

taxa_cambio =  5.38
conversao_dolares = valor_reais/taxa_cambio

print(f"De acordo com a taxa atual de câmbio que é 1 USD = {taxa_cambio} BRL, R${valor_reais} é equivalente a ${conversao_dolares:.2f}")
