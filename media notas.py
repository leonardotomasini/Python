NotaUm = float(input("digite a nota um: "))
NotaDois = float(input("digite a nota Dois: "))
NotaTres = float(input("digite a nota Tres: "))
NotaQuatro = float(input("digite a nota Quatro: "))

media = (NotaUm + NotaDois + NotaTres + NotaQuatro) /4
if media < 5: 
    print("o aluno está reprovado")
elif media <7: 
    print("o aluno está em exame")
else:
    print("o aluno está aprovado")




