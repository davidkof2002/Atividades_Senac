# Exercício 1 — Verificar número positivo ou negativo
# Crie uma função chamada verificar_numero.
# Essa função deve receber um número e informar se ele é:
# •	positivo
# •	negativo
# •	ou zero
# Depois, peça um número ao usuário e utilize a função para mostrar o resultado.



verificar_numero = int(input("Digite um número qualquer: "))

if verificar_numero >= 0:
       print(verificar_numero, "Positivo")
elif verificar_numero <= 0:
       print(verificar_numero, "Número é Negativo") 

Feicha_programa = str(input("Deseja feicha programa? SIM / NÂO: "))

if Feicha_programa == "sim":
       print("Àte logo...")
