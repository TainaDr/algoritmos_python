#pergunta ao usuário a temperatura
temperatura_celsius = C = float(input("Informa a temperatura em celsius: "))

#converte o número em celsius para kelvin
calculo_kelvin = K = C + 273.15
#converte o número em celsius para fahrenheit
calculo_fahrenheit = F = 9/5*C + 32
#converte o número em celsius para rankine
calculo_rankine = R = K * 9/5

#exibe os valores do cálculo para o usuário
print("-------------Exibição da Temperatura Avançada-------------")
#exibe os valores do cálculo em kelvin para o usuário
print(f"{temperatura_celsius}°C em Kelvin é {K}°K")
#exibe os valores do cálculo em fahrenheit para o usuário
print(f"{temperatura_celsius}°C em Fahrenheit é {F}°F")
#exibe os valores do cálculo em rankine para o usuário
print(f"{temperatura_celsius}°C em Rankine é {R}°R")