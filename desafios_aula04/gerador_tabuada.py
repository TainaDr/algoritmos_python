print("Gerador de tabuada")

while True: 
    try: 
        numeroTabuada = int(input("Informe o número da tabuada desejada: "))
        multiplicador = int(input("Informe até que número deseja multiplicar: "))
    
        contador = 1
        while contador <= multiplicador:
            tab = numeroTabuada * contador
            print(f"{numeroTabuada} x {contador} = {tab}")
            contador += 1

    except ValueError:
        print("Erro: Digite apenas números inteiros.")
        continue

    novamente = input("Deseja consultar outra tabuada? (s/n): ").strip().lower()
    
    if novamente != "s":
        print("Programa encerrado.")
        break  

#Exercício: Gerador de Tabuada
# Descrição: Crie um programa que gere a tabuada de qualquer número informado pelo usuário. O programa deve:
# Solicitar um número para calcular a tabuada.
# Perguntar até qual número a tabuada deve ser gerada.
# Exibir a tabuada na tela.
# Perguntar se o usuário deseja gerar outra tabuada. Se sim, repetir o processo; se não, encerrar o programa.