from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://dev.kauansena.com')

@app.route('/calculadora')
def calculadora():
    return render_template('calculator/index.html')

@app.route('/calculadora/resultado', methods=['POST'])
def calculate():
    P0 = float(request.form['P0'])
    P1 = float(request.form['P1'])
    Q0 = float(request.form['Q0'])
    Q1 = float(request.form['Q1'])

    V_Quantidade = (Q1 * 100) / Q0 - 100
    V_preco = (P1 * 100) / P0 - 100
    Elasticidade = V_Quantidade / V_preco
    Valor_modular = abs(Elasticidade)

    if Valor_modular > 1:
        resultado = f'A variação da demanda é de {Valor_modular:.2f}, sendo assim ELÁSTICA'
    elif Valor_modular < 1:
        resultado = f'A variação da demanda é de {Valor_modular:.2f}, sendo assim INELÁSTICA'
    else:
        resultado = f'Sendo a variação igual a {Valor_modular:.2f}, a elasticidade do preço da demanda é UNITÁRIA'

    return render_template('calculator/index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
