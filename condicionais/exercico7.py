
def eh_positivo(num):
    return num > 0


positivos = 0
negativos = 0


for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero == 0:
        print("O número 0 é neutro.")
    elif eh_positivo(numero):
        positivos += 1
    else:
        negativos += 1


print(f"\n--- Resultado Final ---")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
