from flask import Flask, render_template, jsonify

app = Flask(__name__)

# O "Motor" do HISA: Ciência humanizada em trilhas práticas
TRILHA_ATUAL = [
    {
        "dia": 1,
        "tema": "Foco Científico",
        "titulo": "O Mito da Multitarefa",
        "ciencia": "Neurocientistas explicam que o cérebro não foca em duas coisas ao mesmo tempo; ele apenas alterna rápido, gastando 40% mais energia.",
        "pratica": "Escolha UMA tarefa crítica hoje e trabalhe nela por 25 minutos sem abrir o celular."
    },
    {
        "dia": 2,
        "tema": "Hábito",
        "titulo": "A Regra dos 2 Minutos",
        "ciencia": "A dopamina é liberada na conclusão de pequenas metas, não no planejamento de grandes tarefas.",
        "pratica": "Se algo leva menos de 2 minutos, faça agora. Não anote, apenas execute."
    }
]

@app.route('/')
def home():
    # Para o MVP, vamos exibir o Dia 1 como foco principal
    conteudo = TRILHA_ATUAL[0]
    return render_template('index.html', 
                           dia=conteudo['dia'],
                           titulo=conteudo['titulo'], 
                           ciencia=conteudo['ciencia'], 
                           pratica=conteudo['pratica'],
                           tema=conteudo['tema'])

@app.route('/api/trilha')
def api_trilha():
    return jsonify(TRILHA_ATUAL)

if __name__ == '__main__':
    app.run(debug=True)