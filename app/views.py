from flask import render_template, request, Flask
from datetime import datetime
from app import app


@app.route('/')
def home():
    return "<b>Página inicial</b>"

@app.route('/hora')
def template():
    return str(datetime.now())

@app.route('/soma')
def soma():
    return render_template('soma.html')

@app.route('/soma', methods=['POST'])
def my_form_post():
    num1 = request.form['numero1']
    num2 = request.form['numero2']
    return f"A Soma é: {float(num1) + float(num2)}"
