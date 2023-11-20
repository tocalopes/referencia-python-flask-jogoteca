from flask import Flask, render_template

class Jogo:

    def __init__(self, nome, categoraria, console):
        self.nome = nome
        self.categoria = categoraria
        self.console = console

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista_jogos = [Jogo('tetris','puzzle','atari'),
                   Jogo('crash','aventura','ps1')]
    return render_template('lista.html',titulo='Jogos', jogos = lista_jogos)

app.run(port=8080)