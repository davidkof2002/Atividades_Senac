# Exercício 6 — Média de notas
# Crie uma função chamada calcular_media.
# O programa deve:
# 1.	pedir 3 notas ao usuário
# 2.	calcular a média
# 3.	informar se o aluno está:
# •	Aprovado (média ≥ 7)
# •	Recuperação (média entre 5 e 6.9)
# •	Reprovado (média < 5)


nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua pterceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
       print("APROVADO: ")
elif media == 5 and 6.9:
       print("Recuperação: ")
elif media < 5:
       print("Reprovado: ")              