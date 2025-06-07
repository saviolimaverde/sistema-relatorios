from flask import Flask, render_template, request, send_file
from datetime import datetime
import pdfkit
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cliente = request.form["cliente"]
        referencia = request.form["referencia"]
        processos = request.form.getlist("processo")
        andamentos = request.form.getlist("andamento")

        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        processos_completos = zip(processos, andamentos)

        html = render_template(
            "formulario.html",
            cliente=cliente,
            referencia=referencia,
            data_atual=data_atual,
            processos=processos_completos,
        )

        caminho_html = "/tmp/relatorio.html"
        caminho_pdf = "/tmp/relatorio.pdf"

        with open(caminho_html, "w", encoding="utf-8") as f:
            f.write(html)

        pdfkit.from_file(caminho_html, caminho_pdf)
        return send_file(caminho_pdf, as_attachment=True)

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
