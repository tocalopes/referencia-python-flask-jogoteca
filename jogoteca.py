from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    return render_template('lista.html',titulo='Jogos')

app.run(port=8080)