from flask import Flask, render_template, jsonify

app = Flask(__name__)

DISTORCOES_COGNITIVAS = {
    "Generalização Excessiva": {
        "gatilhos": ["sempre", "nunca", "todo mundo"],
        "desafio": "Existem exceções a essa regra? Houve alguma vez em que isso não aconteceu?"
    }
}

@app.route('/')
def home():
    try:
        item = DISTORCOES_COGNITIVAS["Generalização Excessiva"]
        return render_template('index.html', 
                               titulo="Generalização Excessiva", 
                               gatilhos=item["gatilhos"], 
                               desafio=item["desafio"])
    except Exception as e:
        return f"Erro ao carregar o HTML: {e}. Verifique se a pasta 'templates' existe!"

@app.route('/trilha/hoje')
def trilha_do_dia():
    return jsonify(DISTORCOES_COGNITIVAS)

if __name__ == '__main__':
    app.run(debug=True)