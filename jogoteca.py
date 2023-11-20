from flask import Flask, render_template, request


class Jogo:

    def __init__(self, nome, categoraria, console):
        self.nome = nome
        self.categoria = categoraria
        self.console = console


app = Flask(__name__)

lista_jogos = [Jogo('tetris', 'puzzle', 'atari'),
               Jogo('crash', 'aventura', 'ps1')]

@app.route('/inicio')
def inicio():
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
    return inicio()

app.run(port=8080)
