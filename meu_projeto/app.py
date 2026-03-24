from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_mestra_123'

usuarios = {} 
fila = []     

@app.route('/')
def index():
    if 'cpf' in session:
        return render_template('index.html', tela='escolha', nome=session['nome'])
    return render_template('index.html', tela='login')

@app.route('/login', methods=['POST'])
def login():
    nome, cpf = request.form.get('nome'), request.form.get('cpf')
    usuarios[cpf] = nome
    session['cpf'], session['nome'] = cpf, nome
    return redirect(url_for('index'))

@app.route('/entrar_fila')
def entrar_fila():
    cpf, nome = session.get('cpf'), session.get('nome')
    if not any(p for p in fila if p['cpf'] == cpf and p['status'] != 'Finalizado'):
        fila.append({'cpf': cpf, 'nome': nome, 'status': 'Aguardando'})
    return redirect(url_for('ver_paciente'))

@app.route('/paciente')
def ver_paciente():
    cpf = session.get('cpf')
    dados = next((p for p in fila if p['cpf'] == cpf), None)
    return render_template('index.html', tela='paciente', p=dados)

@app.route('/atendente')
def ver_atendente():
    return render_template('index.html', tela='atendente', fila=fila)

@app.route('/mudar_status/<int:idx>')
def mudar_status(idx):
    p = fila[idx]
    p['status'] = 'Em atendimento' if p['status'] == 'Aguardando' else 'Finalizado'
    return redirect(url_for('ver_atendente'))

@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
