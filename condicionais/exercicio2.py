# Exercício 2 — Repetição de mensagem
# Crie uma função chamada mostrar_mensagem.
# Ela deve receber dois parâmetros:
# •	uma mensagem
# •	a quantidade de vezes que ela será exibida
# Use uma estrutura de repetição para imprimir a mensagem várias vezes.
# Exemplo de execução:
# Digite a mensagem: Olá
# Digite quantas vezes deseja mostrar: 3
# Saída esperada:
# Olá
# Olá
# Olá


def mostra_mensagem(mensagem, quantidade):
       for i in range(quantidade):
              print(mensagem)
mensagem1 = input("Digite qualquer coisa: ")
quantidade1 = int(input("Quantas veses que essa mensagem na tela? "))

mostra_mensagem(mensagem1, quantidade1)
       
