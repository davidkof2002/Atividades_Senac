# Estruturas condicionais "while" = enquanto.

# Exemplo: Validação de números positivos

# Para coletar dados do usuarios, use o comando "input"

numero = int(input("Digite um número"))

while numero < 0:
       print("Número inválido. Digite novamente!")
       numero = int(input("Digite um número"))

print("Número válido")       

mensagem1 = input("Digite qualquer coisa: ")

for i in range(3):
       print(mensagem1)