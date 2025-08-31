#Primeiro problema.
#Analise a quantida de sementes utilizadas em uma safra. Informe se elas forem inferior, iguais ou superiores a quantidades de sementes utilizadas. 
while True:
    sementes_plantadas = int(input("Digite a quantidade de sementes plantadas: "))
   
    sementes_colhidas = int(input("Digite a quantidade de sementes colhidas: "))

    if sementes_colhidas == sementes_plantadas:
        print("Colheu exatamente o que plantou")
    elif sementes_colhidas < sementes_plantadas:
        print("Colheu menos sementes do que plantou.")
        diferenca = sementes_colhidas - sementes_plantadas
        print("Você obteve:",diferenca,"a menos")
    else:
        print("Colheu mais sementes do que plantou.")
        diferenca = sementes_colhidas - sementes_plantadas
        print("Você obteve:",diferenca,"a mais")


#Segundo problema.

#Realizar um programa que faça tabuadas até o 10 e finalize quando utiliza um numero negativo.
while True:
    numero = int(input("Digite um número inteiro. Caso escreva um negativo o programa finaliza: "))
   
    if numero < 0:
        print("Encerrando o programa.")
    else:
        print("A tabuada do", numero, "é")
        contador = 1
        while contador <= 10:
            tabuada = numero * contador
            print(tabuada)
            contador += 1

#Terceiro problema

#Crie um programa que peça o peso da pessoa e o peso que ela deseja. O programa finaliza se o peso real for o mesmo que o desejado. Caso abaixa ou acima do peso é necessário
#informar a quantidade de diferença.
while True:
    peso_atual = float(input("Digite o seu peso atual: "))
    peso_desejado = float(input("Digite o peso que deseja: "))
   
    if peso_atual == peso_desejado:
        print("Você já está no peso desejado.")
        break
    elif peso_atual < peso_desejado:
        diferenca = peso_desejado - peso_atual
        print("Você precisa ganhar", diferenca, "kg para chegar ao ideal.")
    else:
        diferenca = peso_atual - peso_desejado
        print("Você precisa perder", diferenca, "kg para chegar ao ideal.")
   
print("Encerrando programa")

