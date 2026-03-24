class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self._salario = salario

    def get_salario(self):
        return self._salario

    def definir_salario(self, novo_salario):
        if novo_salario <= 0:
            raise ValueError("Salário deve ser maior que zero.")
        self._salario = novo_salario

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}, Salário: R$ {self._salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def executar_funcao(self):
        print("Gerente: Aprovando projetos.")


class Atendente(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def executar_funcao(self):
        print("Atendente: Atendendo clientes.")


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)

    def executar_funcao(self):
        print("Desenvolvedor: Desenvolvendo sistemas.")


if __name__ == "__main__":
   
    gerente = Gerente("João Silva", "001", 15000.00)
    atendente = Atendente("Maria Santos", "002", 3000.00)
    desenvolvedor = Desenvolvedor("Pedro Oliveira", "003", 8000.00)

    
    print("=== Demonstração de Encapsulamento ===")
    print(f"Salário inicial dev: R$ {desenvolvedor.get_salario():.2f}")
    desenvolvedor.definir_salario(8500.00)
    print(f"Novo salário dev: R$ {desenvolvedor.get_salario():.2f}")
    try:
        gerente.definir_salario(-1000)
    except ValueError as e:
        print(f"Erro esperado: {e}")
    print()

   
    funcionarios = [gerente, atendente, desenvolvedor]

    print("=== Dados e Funções dos Funcionários ===")
    for f in funcionarios:
        f.mostrar_dados()
        f.executar_funcao()
        print("-" * 50)
