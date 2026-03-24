# Exercício 11 — Calculadora com funções
# Crie um programa com menu interativo:
# 1 - Subtração
# 2 - Multiplicação
# 3 - Divisão
# 4 - Potência
# 5 - Raiz Quadrada
# 0 - Sair
# Cada operação deve ser implementada em uma função separada.


def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Não existe raiz de número negativo!"
    return a ** 0.5

while True:
    print("\n--- CALCULADORA ---")
    print("1 - Subtração\n2 - Multiplicação\n3 - Divisão\n4 - Potência\n5 - Raiz Quadrada\n0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Saindo...")
        break
    
    if opcao in ['1', '2', '3', '4']:
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input("Digite o 2º número: "))
        
        if opcao == '1': print(f"Resultado: {subtrair(n1, n2)}")
        elif opcao == '2': print(f"Resultado: {multiplicar(n1, n2)}")
        elif opcao == '3': print(f"Resultado: {dividir(n1, n2)}")
        elif opcao == '4': print(f"Resultado: {potencia(n1, n2)}")
        
    elif opcao == '5':
        n1 = float(input("Digite o número: "))
        print(f"Resultado: {raiz_quadrada(n1)}")
        
    else:
        print("Opção inválida!")
