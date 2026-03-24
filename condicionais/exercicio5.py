# Exercício 5 — Menu simples
# Crie um programa que exiba o seguinte menu:
# 1 - Subtrair
# 2 - Multiplicar
# 3 - Dividir
# 0 - Sair
# O programa deve continuar executando até que o usuário escolha 0.
# Para cada operação, crie uma função específica.


def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b


opcao = -1

while opcao != 0:
    print("\n--- MENU ---")
    print("1 - Subtrair")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Saindo do programa...")
        break
    
    if opcao in [1, 2, 3]:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print(f"Resultado: {subtrair(n1, n2)}")
        elif opcao == 2:
            print(f"Resultado: {multiplicar(n1, n2)}")
        elif opcao == 3:
            print(f"Resultado: {dividir(n1, n2)}")
    else:
        print("Opção inválida! Tente novamente.")


