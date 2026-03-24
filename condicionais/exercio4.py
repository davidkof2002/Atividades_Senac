# Exercício 4 — Soma de números até N
# Crie uma função chamada somar_numeros.
# Essa função deve receber um número N e somar todos os números de 1 até N.
# Exemplo:
# Entrada: 5
# Cálculo: 1 + 2 + 3 + 4 + 5
# Saída: 15
# ________________________________________

def somar_numeros (n):
       soma = 0
       for i in range(1, n + 1):
              soma = soma + i
       return soma
       
num = int(input("Digite um número: "))
resultado = somar_numeros(num)
print(f"A soma de 1 até {num} é: {resultado}") 


