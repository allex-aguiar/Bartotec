import flask
from flask import Flask, render_template, request

app = flask.Flask(__name__)


# ==========================================
# ORÇAMENTO DO JOGO
# ==========================================

ORCAMENTO = 5000


# ==========================================
# PEÇAS DO COMPUTADOR
# ==========================================

pecas = {

    # PROCESSADORES

    "cpu1": {
        "nome": "Processador Básico",
        "preco": 600,
        "pontos": 10
    },

    "cpu2": {
        "nome": "Processador Gamer",
        "preco": 1000,
        "pontos": 20
    },

    "cpu3": {
        "nome": "Processador Pro",
        "preco": 1500,
        "pontos": 30
    },


    # PLACAS DE VÍDEO

    "gpu1": {
        "nome": "GPU Básica",
        "preco": 900,
        "pontos": 15
    },

    "gpu2": {
        "nome": "GPU Gamer",
        "preco": 1500,
        "pontos": 25
    },

    "gpu3": {
        "nome": "GPU Ultra",
        "preco": 2200,
        "pontos": 40
    },


    # MEMÓRIA RAM

    "ram1": {
        "nome": "8 GB",
        "preco": 250,
        "pontos": 5
    },

    "ram2": {
        "nome": "16 GB",
        "preco": 450,
        "pontos": 10
    },

    "ram3": {
        "nome": "32 GB",
        "preco": 800,
        "pontos": 20
    },


    # ARMAZENAMENTO

    "ssd1": {
        "nome": "SSD 500 GB",
        "preco": 300,
        "pontos": 5
    },

    "ssd2": {
        "nome": "SSD 1 TB",
        "preco": 500,
        "pontos": 10
    },

    "ssd3": {
        "nome": "SSD 2 TB",
        "preco": 850,
        "pontos": 15
    },


    # FONTES

    "fonte1": {
        "nome": "Fonte 500W",
        "preco": 300,
        "pontos": 5
    },

    "fonte2": {
        "nome": "Fonte 650W",
        "preco": 450,
        "pontos": 10
    },

    "fonte3": {
        "nome": "Fonte 750W",
        "preco": 600,
        "pontos": 15
    },


    # MONITORES

    "monitor1": {
        "nome": "Monitor Full HD",
        "preco": 700,
        "pontos": 10
    },

    "monitor2": {
        "nome": "Monitor Gamer 144Hz",
        "preco": 1100,
        "pontos": 20
    },

    "monitor3": {
        "nome": "Monitor Gamer 240Hz",
        "preco": 1600,
        "pontos": 30
    }
}


# ==========================================
# PÁGINA INICIAL
# ==========================================

@app.route("/")
def inicio():
    return flask.render_template("index.html")


# ==========================================
# FINALIZAR DESAFIO
# ==========================================

@app.route("/jogar", methods=["POST"])
def jogar():

    # Recebe as escolhas feitas no index.html

    processador = flask.request.form["processador"]

    placa_video = flask.request.form["placa_video"]

    ram = flask.request.form["ram"]

    armazenamento = flask.request.form["armazenamento"]

    fonte = flask.request.form["fonte"]

    monitor = flask.request.form["monitor"]


    # ======================================
    # JUNTA AS ESCOLHAS
    # ======================================

    escolhas = [
        processador,
        placa_video,
        ram,
        armazenamento,
        fonte,
        monitor
    ]


    # ======================================
    # CALCULA O PREÇO E O DESEMPENHO
    # ======================================

    total = 0
    pontuacao = 0


    for escolha in escolhas:

        total = total + pecas[escolha]["preco"]

        pontuacao = pontuacao + pecas[escolha]["pontos"]


    # ======================================
    # CALCULA O ORÇAMENTO RESTANTE
    # ======================================

    restante = ORCAMENTO - total


    # ======================================
    # VERIFICA O RESULTADO
    # ======================================

    if total <= ORCAMENTO:

        resultado = "Parabéns! Você montou o PC dentro do orçamento!"

    else:

        resultado = "Você ultrapassou o orçamento de R$ 5.000!"


    # ======================================
    # DEFINE O NÍVEL DE DESEMPENHO
    # ======================================

    if pontuacao >= 100:

        desempenho = "Excelente"

    elif pontuacao >= 70:

        desempenho = "Muito bom"

    elif pontuacao >= 50:

        desempenho = "Bom"

    else:

        desempenho = "Básico"


    # ======================================
    # ENVIA TUDO PARA RESULTADO.HTML
    # ======================================

    return flask.render_template(
        "resultado.html",

        total=total,

        orcamento=ORCAMENTO,

        restante=restante,

        pontuacao=pontuacao,

        desempenho=desempenho,

        resultado=resultado
    )


# ==========================================
# INICIA O FLASK
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)