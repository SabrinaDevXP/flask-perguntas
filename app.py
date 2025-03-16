from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

perguntas = [
    "Mana você é ygona?",
    "Se pudesse jantar com qualquer pessoa no mundo, viva ou morta, quem seria?",
]

perguntas_restantes = perguntas.copy()
perguntas_sorteadas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sortear')
def sortear_pergunta():
    global perguntas_restantes, perguntas_sorteadas
    if not perguntas_restantes:
        perguntas_restantes = perguntas.copy()
        perguntas_sorteadas.clear()
    pergunta = random.choice(perguntas_restantes)
    perguntas_restantes.remove(pergunta)
    perguntas_sorteadas.append(pergunta)
    return jsonify({'pergunta': pergunta})

@app.route('/voltar')
def voltar_pergunta():
    if len(perguntas_sorteadas) > 1:
        pergunta_atual = perguntas_sorteadas.pop()
        perguntas_restantes.insert(0, pergunta_atual)
        return jsonify({'pergunta': perguntas_sorteadas[-1]})
    return jsonify({'pergunta': perguntas_sorteadas[0] if perguntas_sorteadas else "Clique para sortear uma pergunta"})

if __name__ == '__main__':
    app.run(debug=True)