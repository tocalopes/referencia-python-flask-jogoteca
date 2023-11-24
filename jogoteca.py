from flask import Flask, render_template, request, redirect


class Jogo:

    def __init__(self, nome, categoraria, console):
        self.nome = nome
        self.categoria = categoraria
        self.console = console


app = Flask(__name__)

lista_jogos = [Jogo('tetris', 'puzzle', 'atari'),
               Jogo('crash', 'aventura', 'ps1')]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar',methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect('/')

app.run(port=8080, debug=True)
