'''
caminho = "./Desktop/aula/dados.txt.txt"
with open (caminho, 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
'''

'''
frases = open("./Desktop/aula/frases.txt", "r")
for x in frases:
    print(frases)
'''

'''
caminho = "./Desktop/aula/dados.txt.txt"
with open (caminho, 'r') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
'''

'''
from collections import Counter
caminho = "./Desktop/aula/texto.txt"
with open (caminho, 'r') as arquivo:
    conteudo = arquivo.read()
palavras = conteudo.split()
quantidade = len(palavras)
print(f'o arquivo "texto.txt" contém {quantidade} palavras.')
contagem = Counter(palavras)
frequentes = contagem.most_common(5)
print("As 5 palavras mais frequentes são")
for palavra, frequencia in frequentes: 
    print(f'{palavra}: {frequencia} vezes')
'''

'''
palavra = input("Digite a palavra que quer procurar ").strip().lower()
encontrado = False
caminho = "./Desktop/aula/texto.txt"
with open(caminho, 'r', encoding = ' utf') as arquivo:
    for numero_linha, linha in enumerate(arquivo, start=1):
        if palavra in linha.lower():
            encontrado = True
            print(f'a palavra "{palavra}" está na linha {numero_linha}:')
            print(linha.strip())
'''

'''
from collections import Counter
caminho = "./Desktop/aula/texto.txt"
def calcular_estatisticas(arquivo):
    with open(arquivo, 'r', encoding='utf') as f:
        conteudo = f.read()
    linhas = conteudo.splitlines()
    palavras = conteudo.split()
    caracteres = len(conteudo)
    maiusculas = sum(1 for c in conteudo if c.isupper())
    minusculas = sum(1 for c in conteudo if c.islower())
    digitos = sum(1 for c in conteudo if c.isdigit())
    espacos = sum(1 for c in conteudo if c.isspace())
    print(f'quantidade linhas: {len(linhas)}')
    print(f'quantidade palavras: {len(palavras)}')
    print(f'quantidade caracteres: {caracteres}')
    print(f'quantidade letras maiúsculas: {maiusculas}')
    print(f'quantidade letras minúsculas: {minusculas}')
    print(f'quantidade dígitos: {digitos}')
    print(f'quantidade espaços em branco: {espacos}')
calcular_estatisticas(caminho)
'''

'''
import json
alunos = []
adicionar_nota = True
while adicionar_nota:
    nome = input("nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f'nota {i+1}: '))
        notas.append(nota)
    alunos.append({'nome': nome, 'notas': notas})
    resposta = input("adicionar outro aluno? (sim/não): ").strip().lower()
    adicionar_nota = (resposta == 'sim')
with open('./Desktop/aula/notas.json', 'w') as file:
    json.dump(alunos, file, indent=4)



import json
with open('notas.json', 'r') as file:
    alunos = json.load(file)
for aluno in alunos:
    media = sum(aluno['notas']) / len(aluno['notas'])
    aluno['media'] = media
    aluno['exame'] = media < 6.0
with open('notas.json', 'w') as file:
    json.dump(alunos, file, indent=4)
for aluno in alunos:
    print(f"nome: {aluno['nome']}, média: {aluno['media']}, em exame: {'sim' if aluno['exame'] else 'não'}") 


import json
with open('notas.json', 'r') as file:
    alunos = json.load(file)
for aluno in alunos:
    if aluno['exame']:
        nota_exame = float(input(f"Nota de exame do aluno {aluno['nome']}: "))
        aluno['nota_exame'] = nota_exame
        media_final = (aluno['media'] + nota_exame) / 2
        aluno['media_final'] = media_final
        aluno['condicao'] = 'Aprovado por exame' if media_final >= 6.0 else 'Reprovado'
    else:
        aluno['nota_exame'] = None
        aluno['media_final'] = aluno['media']
        aluno['condicao'] = 'Aprovado'
alunos = sorted(alunos, key=lambda x: x['nome'])
with open('boletim.json', 'w') as file:
    json.dump(alunos, file, indent=4)
'''