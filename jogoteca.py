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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
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
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'senha' == request.form['senha']:
        usuario = request.form['usuario']
        session['usuario_logado'] = usuario
        flash(usuario + 'logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado')
        return redirect('/login')


app.run(port=8080, debug=True)
