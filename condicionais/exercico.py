# Exercício 10 — Soma de números pares
# Crie uma função chamada somar_pares.
# O programa deve:
# 1.	pedir números ao usuário 5 vezes
# 2.	somar apenas os números pares
# Ao final, mostrar o valor total da soma.

def somar_pares():
    soma = 0
    for i in range(5):
        num = int(input(f"Digite o número: "))
        if num % 2 == 0:
            soma += num
    
    print(f"A soma dos números pares é: {soma}")
somar_pares()



              