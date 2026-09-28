from flask import Flask, render_template, request

app = Flask(__name__)


# Orçamento máximo do jogador
ORCAMENTO = 5000


# Peças disponíveis no jogo
pecas = {

    # Processadores
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


    # Placas de vídeo
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


    # Memória RAM
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


    # Armazenamento
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


    # Fontes
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


    # Monitores
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


# Página inicial
@app.route("/jogar")
def inicio():

    return render_template("index.html")


# Recebe as escolhas do jogador
@app.route("/jogar", methods=["POST"])
def jogar():

    # Recebe as peças escolhidas no HTML
    processador = request.form["processador"]
    placa_video = request.form["placa_video"]
    ram = request.form["ram"]
    armazenamento = request.form["armazenamento"]
    fonte = request.form["fonte"]
    monitor = request.form["monitor"]


    # Coloca todas as escolhas em uma lista
    escolhas = [
        processador,
        placa_video,
        ram,
        armazenamento,
        fonte,
        monitor
    ]


    # Começa o preço e a pontuação em zero
    total = 0
    pontuacao = 0


    # Soma os preços e os pontos das peças
    for escolha in escolhas:

        total = total + pecas[escolha]["preco"]

        pontuacao = pontuacao + pecas[escolha]["pontos"]


    # Verifica se o jogador ficou dentro do orçamento
    if total <= ORCAMENTO:

        resultado = "Parabéns! Você montou o PC dentro do orçamento!"

    else:

        resultado = "Você ultrapassou o orçamento de R$ 5.000!"


    # Envia os resultados para resultado.html
    return render_template(
        "resultado.html",
        total=total,
        pontuacao=pontuacao,
        resultado=resultado
    )


# Inicia o servidor
if __name__ == "__main__":

    app.run(debug=True)