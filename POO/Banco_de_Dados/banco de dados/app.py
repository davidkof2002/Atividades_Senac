import sqlite3  # Importa o módulo para trabalhar com banco de dados SQLite

# Importa as funções necessárias do framework Flask para criar a aplicação web
from flask import Flask, redirect, render_template, request, url_for


class BancoLivros:
    """
    Classe única do back-end.
    Ela concentra a conexão e os comandos SQL do projeto.
    """

    def __init__(self, nome_banco):
        self.nome_banco = nome_banco  # Armazena o nome do arquivo do banco de dados
        self.criar_tabela()  # Chama o método para garantir que a tabela exista ao iniciar

    def conectar(self):
        # Abre uma conexão com o arquivo do banco de dados
        conexao = sqlite3.connect(self.nome_banco)
        # Configura para retornar os resultados como dicionários (acesso pelo nome da coluna)
        conexao.row_factory = sqlite3.Row
        return conexao

    def criar_tabela(self):
        # Comando SQL para criar a tabela 'livros' caso ela ainda não tenha sido criada
        sql = """
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL
        )
        """
        with self.conectar() as conexao:  # Abre a conexão
            conexao.execute(sql)         # Executa o comando de criação
            conexao.commit()             # Salva as alterações no arquivo

    def adicionar(self, titulo, autor, ano):
        # Comando SQL para inserir um novo livro usando '?' para evitar ataques de SQL Injection
        sql = "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)"
        with self.conectar() as conexao:
            conexao.execute(sql, (titulo, autor, ano)) # Executa passando os dados recebidos
            conexao.commit()                           # Confirma a inserção

    def listar(self, busca=""):
        # Comando SQL para buscar livros cujo título contenha o termo pesquisado (LIKE)
        sql = """
        SELECT * FROM livros
        WHERE titulo LIKE ?
        ORDER BY titulo
        """
        with self.conectar() as conexao:
            # O f"%{busca}%" permite encontrar o termo em qualquer parte da frase
            return conexao.execute(sql, (f"%{busca}%",)).fetchall()

    def buscar_por_id(self, id):
        # Comando SQL para localizar um registro específico através do seu ID único
        sql = "SELECT * FROM livros WHERE id = ?"
        with self.conectar() as conexao:
            return conexao.execute(sql, (id,)).fetchone() # Retorna apenas um resultado

    def atualizar(self, id, titulo, autor, ano):
        # Comando SQL para modificar os dados de um livro que já existe
        sql = "UPDATE livros SET titulo = ?, autor = ?, ano = ? WHERE id = ?"
        with self.conectar() as conexao:
            conexao.execute(sql, (titulo, autor, ano, id))
            conexao.commit() # Salva as alterações da edição

    def excluir(self, id):
        # Comando SQL para remover um registro permanentemente pelo ID
        sql = "DELETE FROM livros WHERE id = ?"
        with self.conectar() as conexao:
            conexao.execute(sql, (id,))
            conexao.commit() # Confirma a remoção

    def contar(self):
        # Comando SQL para contar o número total de registros na tabela
        sql = "SELECT COUNT(*) AS total FROM livros"
        with self.conectar() as conexao:
            return conexao.execute(sql).fetchone()["total"] # Retorna o valor numérico


app = Flask(__name__)  # Cria a instância da aplicação Flask
banco = BancoLivros("biblioteca.db")  # Instancia a classe do banco definindo o nome do arquivo


@app.route("/") # Define que esta função responde à URL principal (Home)
def index():
    # Pega o termo de busca vindo da URL (ex: ?busca=harry)
    busca = request.args.get("busca", "")
    # Pega o ID do livro caso o usuário tenha clicado em "Editar"
    editar_id = request.args.get("editar")

    # Se houver um ID para editar, busca os dados desse livro, senão fica vazio
    livro_edicao = banco.buscar_por_id(editar_id) if editar_id else None
    livros = banco.listar(busca) # Lista todos os livros (ou os filtrados pela busca)
    total = banco.contar()       # Pega a contagem total para exibir na tela

    # Renderiza o arquivo HTML passando todas as variáveis necessárias para o front-end
    return render_template(
        "index.html",
        livros=livros,
        total=total,
        busca=busca,
        livro_edicao=livro_edicao,
    )


@app.route("/adicionar", methods=["POST"]) # Rota que recebe dados via formulário (POST)
def adicionar():
    # Chama o método de adicionar pegando os valores dos campos do formulário HTML
    banco.adicionar(
        request.form["titulo"],
        request.form["autor"],
        int(request.form["ano"]), # Converte o ano para número inteiro
    )
    return redirect(url_for("index")) # Recarrega a página inicial para mostrar o novo livro


@app.route("/atualizar/<int:id>", methods=["POST"]) # Rota para salvar a edição de um livro
def atualizar(id):
    # Envia os novos dados do formulário para o método atualizar do banco
    banco.atualizar(
        id,
        request.form["titulo"],
        request.form["autor"],
        int(request.form["ano"]),
    )
    return redirect(url_for("index")) # Volta para a tela principal


@app.route("/excluir/<int:id>", methods=["POST"]) # Rota para deletar um livro
def excluir(id):
    banco.excluir(id) # Chama a função de exclusão passando o ID da URL
    return redirect(url_for("index")) # Atualiza a página


if __name__ == "__main__":
    # Inicia o servidor local do Flask em modo de depuração (mostra erros no navegador)
    app.run(debug=True)
