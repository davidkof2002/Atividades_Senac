# Exercício 5 — Sistema de animais de uma clínica veterinária
# Enunciado
# Uma clínica veterinária quer registrar animais atendidos.
# Todo animal possui:
# •	nome
# •	idade
# •	peso
# Crie uma classe Animal com métodos para:
# •	mostrar dados
# •	emitir som
# Depois, crie três subclasses:
# •	Cachorro
# •	Gato
# •	Papagaio
# Cada uma deve:
# •	emitir um som diferente
# •	ter um método específico:
# o	cachorro → abanar_rabo()
# o	gato → arranhar()
# o	papagaio → falar()
# Além disso, proteja os dados do animal para que idade e peso não recebam valores inválidos.
# O que esse exercício desenvolve
# Esse exercício trabalha muito bem:
# •	abstração
# •	herança
# •	polimorfismo
# •	encapsulamento
# Dica para os alunos
# Não basta só criar as classes.
# Eles devem pensar:
# •	como impedir idade negativa?
# •	como impedir peso zero ou negativo?
# •	como acessar os dados de forma segura?


class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.definir_idade(idade)
        self.definir_peso(peso)

    def definir_idade(self, nova_idade):
        if nova_idade >= 0:
            self.idade = nova_idade
        else:
            print("Erro: A idade não pode ser negativa! Definindo como 0.")
            self.idade = 0

    def definir_peso(self, novo_peso):
        if novo_peso > 0:
            self.peso = novo_peso
        else:
            print("Erro: O peso deve ser maior que zero! Definindo como 1kg.")
            self.peso = 1

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} anos | Peso: {self.peso}kg")

    def emitir_som(self):
        print("O animal faz um som qualquer.")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Au Au!")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo feliz!")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self.nome} diz: Miau!")

    def arranhar(self):
        print(f"{self.nome} arranhou o sofá!")


class Papagaio(Animal):
    def emitir_som(self):
        print(f"{self.nome} faz barulhos de pássaro!")

    def falar(self):
        print(f"{self.nome} diz: 'Loro quer biscoito!'")



print("--- Cadastrando o Rex ---")
dog = Cachorro("Rex", 5, 15)
dog.mostrar_dados()
dog.emitir_som()
dog.abanar_rabo()

print("\n--- Cadastrando a Luna (com idade errada) ---")
cat = Gato("Luna", -2, 4) 
cat.mostrar_dados()
cat.emitir_som()
cat.arranhar()

print("\n--- Cadastrando o Louro ---")
ave = Papagaio("Louro José", 10, 0.5)
ave.mostrar_dados()
ave.falar()
