minutos = int(input("Informe um valor em minutos: "))

horas = minutos // 60  
minutos_restantes = minutos % 60  

print(f"{minutos} minutos é equivalente a: {horas} horas e {minutos_restantes} minutos - {horas}:{minutos_restantes}.")
