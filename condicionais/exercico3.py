# Exercício 3 — Contar números pares
# Crie uma função chamada verificar_par.
# A função deve receber um número e retornar se ele é par ou ímpar.
# Depois, peça 5 números ao usuário utilizando uma estrutura de repetição.
# Ao final, informe:
# •	quantos números pares foram digitados

def verificar_par(num1):
       if num1 % 2 == 0:
              return True
       else:
              return False
       
total_pares = 0


for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if verificar_par(num):
        total_pares += 1
    
    
    

print(f"\nVocê digitou {total_pares} números pares.")                    


