numero = int(input("digite um numero :"))
if numero % 3 == 0 and numero % 7 == 0:
    print("O número é múltiplo de 3 e 7 ao mesmo tempo.")
elif numero % 3 == 0:
    print("o numero é multiplo de 3")
elif numero % 7 == 0:
    print("o numero é multiplo de 7")
else:
    print("o numero não é multiplo de 3 ou 7")