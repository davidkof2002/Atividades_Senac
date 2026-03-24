# Exercício 8 — Tabuada completa
# Crie uma função chamada mostrar_tabuada.
# A função deve receber um número e mostrar sua tabuada de 1 até 10.
# Depois crie um programa que:
# 1.	peça um número
# 2.	chame a função para exibir a tabuada


def mostra_tabuada(numero):
  for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
  for i in range(1, 11):
    print(numero, "-", i, "=", numero - i)
  for i in range(1, 11):    
    print(numero, "/", i, "=", numero / i)
  for i in range(1, 11):    
    print(numero, "+", i, "=", numero + i)

n = int(input("Digite um número: "))

mostra_tabuada(n)