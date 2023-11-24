import random

from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:

    def __init__(self, nome, categoraria, console):
        self.nome = nome
        self.categoria = categoraria
        self.console = console


app = Flask(__name__)

lista_participantes = []
vencedor = ""


@app.route('/')
def index():
    return render_template('lista.html', titulo='Participante', participantes=lista_participantes)

@app.route('/vencedor', methods=['POST','GET'])
def vencedor():
    vencedor = request.args.get('vencedor')
    return render_template('lista.html', titulo='Vencedor', participantes=lista_participantes, vencedor=vencedor)


@app.route('/novo', methods=['POST', 'GET'])
def novo():
    return render_template('novo.html', titulo='Cadastrar participante')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    lista_participantes.append(nome)
    return redirect(url_for('index'))


@app.route('/zerar', methods=['POST'])
def zerar():
    lista_participantes = []
    vencedor = None
    return redirect(url_for('index'))

@app.route('/sortear', methods=['POST'])
def sortear():
    vencedor = random.choice(lista_participantes)
    lista_participantes.clear()
    return redirect(url_for('vencedor', vencedor=vencedor))


app.run(port=8080, debug=True)
