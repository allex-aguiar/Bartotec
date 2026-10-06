from flask import Flask, render_template, request

app = Flask(__name__)

# Orçamento máximo
ORCAMENTO = 5000


# Preços das peças
precos = {
    "processador": {
        "cpu1": 600,
        "cpu2": 1000,
        "cpu3": 1500
    },

    "placa_video": {
        "gpu1": 900,
        "gpu2": 1500,
        "gpu3": 2200
    },

    "ram": {
        "ram1": 250,
        "ram2": 450,
        "ram3": 800
    },

    "armazenamento": {
        "ssd1": 300,
        "ssd2": 500,
        "ssd3": 850
    },

    "fonte": {
        "fonte1": 300,
        "fonte2": 450,
        "fonte3": 600
    },

    "monitor": {
        "monitor1": 700,
        "monitor2": 1100,
        "monitor3": 1600
    }
}


# Pontuação de cada peça
pontos = {
    "processador": {
        "cpu1": 10,
        "cpu2": 20,
        "cpu3": 30
    },

    "placa_video": {
        "gpu1": 15,
        "gpu2": 25,
        "gpu3": 40
    },

    "ram": {
        "ram1": 5,
        "ram2": 10,
        "ram3": 20
    },

    "armazenamento": {
        "ssd1": 5,
        "ssd2": 10,
        "ssd3": 15
    },

    "fonte": {
        "fonte1": 5,
        "fonte2": 10,
        "fonte3": 15
    },

    "monitor": {
        "monitor1": 10,
        "monitor2": 20,
        "monitor3": 30
    }
}


# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Recebe as escolhas do jogador
@app.route("/jogar", methods=["POST"])
def jogar():

    escolhas = {
        "processador": request.form.get("processador"),
        "placa_video": request.form.get("placa_video"),
        "ram": request.form.get("ram"),
        "armazenamento": request.form.get("armazenamento"),
        "fonte": request.form.get("fonte"),
        "monitor": request.form.get("monitor")
    }


    # Calcula o valor total das peças
    total = sum(
        precos[categoria][valor]
        for categoria, valor in escolhas.items()
    )


    # Verifica se ultrapassou o orçamento
    if total > ORCAMENTO:

        return render_template(
            "resultado.html",
            total=total,
            orcamento=ORCAMENTO,
            falhou=True
        )


    # Calcula a pontuação
    pontuacao = sum(
        pontos[categoria][valor]
        for categoria, valor in escolhas.items()
    )


    # Define o desempenho
    if pontuacao >= 100:
        desempenho = "Excelente!"

    elif pontuacao >=85:
        desempenho = "Muito bom!"

    else:
        desempenho = "Pode melhorar!"


    # Mostra o resultado
    return render_template(
        "resultado.html",
        total=total,
        orcamento=ORCAMENTO,
        pontuacao=pontuacao,
        desempenho=desempenho,
        falhou=False
    )


# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
