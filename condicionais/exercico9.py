def verificar_senha():
    correta = "senac"
    tentativas = 3

    for i in range(tentativas):
        senha_digitada = input(f"Digite a senha: ")
        
        if senha_digitada == correta:
            print("Acesso permitido")
            return 
            
    print("Conta bloqueada")

verificar_senha()

