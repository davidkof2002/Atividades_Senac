# Exercício 1 — Sistema de veículos de entrega
# Enunciado
# Uma empresa de entregas deseja cadastrar veículos utilizados pelos funcionários.
# Todos os veículos possuem:
# •	marca
# •	modelo
# •	ano
# Porém, cada tipo de veículo possui comportamentos próprios:
# •	Carro → deve exibir que está transportando várias encomendas
# •	Moto → deve exibir que está fazendo entrega rápida
# •	Bicicleta → deve exibir que está realizando entrega ecológica
# Crie:
# •	uma classe base chamada Veiculo
# •	três classes filhas:
# o	Carro
# o	Moto
# o	Bicicleta
# A classe base deve possuir um método para mostrar os dados do veículo.
# Cada classe filha deve implementar seu próprio método realizar_entrega().
# Depois,  (PESQUISA) crie pelo menos um objeto de cada tipo e mostre suas informações e sua ação de entrega.
# O que esse exercício desenvolve
# Esse exercício força o aluno a perceber:
# •	o que é comum entre objetos diferentes
# •	o que deve ficar na classe mãe
# •	o que deve ser especializado nas classes filhas
# •	como funciona herança
# •	como funciona polimorfismo
# Dica para os alunos
# Pensem assim:
# “Todo carro é um veículo, toda moto é um veículo, toda bicicleta é um veículo.”
# Então o que é igual deve subir para a superclasse.


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_dados(self):
        print(f"Veículo: {self.marca} {self.modelo} - {self.ano}")

    def realizar_entrega(self):
        raise NotImplementedError("Método deve ser implementado pelas subclasses")


class Carro(Veiculo):
    def realizar_entrega(self):
        print(f"{self.marca} {self.modelo} está transportando várias encomendas.")


class Moto(Veiculo):
    def realizar_entrega(self):
        print(f"{self.marca} {self.modelo} está fazendo entrega rápida.")


class Bicicleta(Veiculo):
    def realizar_entrega(self):
        print(f"{self.marca} {self.modelo} está realizando entrega ecológica.")


if __name__ == "__main__":
    
    carro = Carro("Toyota", "Corolla", 2020)
    moto = Moto("Honda", "CG 160", 2023)
    bicicleta = Bicicleta("Caloi", "Envoy", 2022)

   
    veiculos = [carro, moto, bicicleta]

    for v in veiculos:
        v.mostrar_dados()
        v.realizar_entrega()
        print("-" * 40)
