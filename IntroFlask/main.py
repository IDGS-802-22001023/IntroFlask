from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "IDGS-802-Flask"
    lista = ['Juan', 'Karla', 'Miguel', 'Ana']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route("/operaBas")
def operas1():
    return render_template("operaBas.html")

@app.route("/resultado", methods=("GET", "POST"))
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    operacion = request.form.get("operacion")


    if operacion == "dividir":
        if n2 == 0:
            return "Error: no se puede dividir entre cero"
        resultado = n1 / n2

    elif operacion == "restar":
        resultado = n1 - n2

    elif operacion == "sumar":
        resultado = n1 + n2

    elif operacion == "multiplicar":
        resultado = n1 * n2

    else:
        return "Operación no válida"

    return f"El resultado es: {resultado}"


    
@app.route('/formulario')
def formulario():
    return render_template("formularios.html")

@app.route('/reportes')
def reportes():
    return render_template("reportes.html")

@app.route('/hola')
def hola():
    return "Hola, Hola"

@app.route('/user/<string:user>')
def user(user):
    return f"Hello, {user}!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param="Juan"):
    return f"<h1>¡Hola, {param}!</h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
            <label>Name:</label>
            <input type="text" name="name" required><br><br>

            <label>Apellido paterno:</label>
            <input type="text" name="apaterno" required>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
