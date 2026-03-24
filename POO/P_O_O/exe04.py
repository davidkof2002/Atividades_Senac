# Exercício 4 — Sistema de personagens de jogo
# Enunciado
# Você vai criar um sistema simples de personagens para um jogo.
# Todo personagem possui:
# •	nome
# •	vida
# •	nível
# Crie uma classe base Personagem com métodos para:
# •	mostrar status
# •	atacar
# Depois, crie três classes filhas:
# •	Guerreiro
# •	Mago
# •	Arqueiro
# Cada um deve atacar de maneira diferente:
# •	Guerreiro → ataque físico pesado
# •	Mago → magia
# •	Arqueiro → disparo à distância
# Além disso, (PESQUISA) crie um método chamado habilidade_especial() em cada classe filha com comportamento próprio.
# Depois, instancie pelo menos um personagem de cada tipo e mostre as ações.
# O que esse exercício desenvolve
# Esse exercício é ótimo porque costuma engajar mais os alunos.
# Além disso, desenvolve:
# •	modelagem de objetos
# •	herança
# •	polimorfismo
# •	especialização de comportamento
# Dica para os alunos
# Tentem identificar:

# Classe principal (Pai)
class Personagem:
    def __init__(self, nome, vida, nivel):
        self.nome = nome
        self.vida = vida
        self.nivel = nivel

    def mostrar_status(self):
        print("--- Status do Personagem ---")
        print("Nome:", self.nome)
        print("Vida:", self.vida)
        print("Nível:", self.nivel)

    def atacar(self):
        print(self.nome, "realizou um ataque básico!")

# Classe Guerreiro (Filha)
class Guerreiro(Personagem):
    def atacar(self):
        print(self.nome, "usou sua espada para um ATAQUE FÍSICO PESADO!")

    def habilidade_especial(self):
        print(self.nome, "usou o Grito de Guerra: Defesa aumentada!")


class Mago(Personagem):
    def atacar(self):
        print(self.nome, "lançou uma BOLA DE FOGO mágica!")

    def habilidade_especial(self):
        print(self.nome, "usou a Cura Arcana: Recuperou um pouco de vida!")


class Arqueiro(Personagem):
    def atacar(self):
        print(self.nome, "fez um DISPARO À DISTÂNCIA com seu arco!")

    def habilidade_especial(self):
        print(self.nome, "usou a Chuva de Flechas: Acertou todos os inimigos!")




heroi1 = Guerreiro("Thorin", 150, 5)
heroi1.mostrar_status()
heroi1.atacar()
heroi1.habilidade_especial()

print("\n") 


heroi2 = Mago("Gandalf", 80, 10)
heroi2.mostrar_status()
heroi2.atacar()
heroi2.habilidade_especial()

print("\n")


heroi3 = Arqueiro("Legolas", 100, 8)
heroi3.mostrar_status()
heroi3.atacar()
heroi3.habilidade_especial()

