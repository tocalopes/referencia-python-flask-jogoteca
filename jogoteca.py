from flask import Flask, render_template, request, redirect, session, flash


class Jogo:

    def __init__(self, nome, categoraria, console):
        self.nome = nome
        self.categoria = categoraria
        self.console = console


app = Flask(__name__)
app.secret_key = 'tocalopes'

lista_jogos = [Jogo('tetris', 'puzzle', 'atari'),
               Jogo('crash', 'aventura', 'ps1')]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'alohomora' == request.form['senha']:
        usuario = request.form['usuario']
        session['usuario_logado'] = usuario
        flash(usuario + 'logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')


app.run(port=8080, debug=True)
