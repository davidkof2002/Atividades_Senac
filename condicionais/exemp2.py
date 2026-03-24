# Exemplo 2: tabuada pesrsonalizda

# Condicionaç "if:" se/ "else": senão
# estruturas de repetição "for" para;
# o "for" necessita de uma varialvel auxiliar e uma condição de para (a,b);
# a = ponto de paritda / b = ponto de para -1

numero = int(input("Digite um número?: "))

if numero == 0:
       print("Tabuada do 0 séra 0.")
else:
       for i in range(1,11):
              resultado = numero * i
              print(resultado)