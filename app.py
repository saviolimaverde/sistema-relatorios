from flask import Flask, render_template
from weasyprint import HTML

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/gerar_pdf')
def gerar_pdf():
    html = render_template('formulario.html')
    HTML(string=html).write_pdf("saida.pdf")
    return "PDF gerado com sucesso!"
