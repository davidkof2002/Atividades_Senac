from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_sessao'

usuarios = {}
fila = []

@app.route('/')
def index():
    if 'cpf' in session:
        return render_template('escolher_papel.html', nome=session['nome'])
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    
    if cpf not in usuarios:
        usuarios[cpf] = nome
    
    session['cpf'] = cpf
    session['nome'] = usuarios[cpf]
    return redirect(url_for('index'))

@app.route('/entrar_fila')
def entrar_fila():
    cpf = session.get('cpf')
    nome = session.get('nome')
    
    ja_esta = any(p for p in fila if p['cpf'] == cpf and p['status'] != 'Atendimento finalizado')
    
    if not ja_esta:
        fila.append({
            'cpf': cpf,
            'nome': nome,
            'status': 'Aguardando atendimento'
        })
    return redirect(url_for('area_paciente'))

@app.route('/paciente')
def area_paciente():
    cpf = session.get('cpf')
    dados_paciente = next((p for p in fila if p['cpf'] == cpf), None)
    return render_template('paciente.html', p=dados_paciente)

@app.route('/atendente')
def area_atendente():
    return render_template('atendente.html', fila=fila)

@app.route('/mudar_status/<int:indice>')
def mudar_status(indice):
    p = fila[indice]
    if p['status'] == 'Aguardando atendimento':
        p['status'] = 'Em andamento'
    elif p['status'] == 'Em andamento':
        p['status'] = 'Atendimento finalizado'
    return redirect(url_for('area_atendente'))

@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
