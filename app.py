from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/compra", methods=["GET", "POST"])
def compra():
    resultado = None
    error = None
    valores = {"cantidad": "", "precio": ""}

    if request.method == "POST":
        valores = {
            "cantidad": request.form.get("cantidad", "").strip(),
            "precio": request.form.get("precio", "").strip(),
        }
        try:
            cantidad = int(valores["cantidad"])
            precio = float(valores["precio"])
            if cantidad <= 0 or precio < 0:
                raise ValueError
            subtotal = cantidad * precio
            descuento = subtotal * 0.10 if subtotal > 1000 else 0
            resultado = {
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal,
                "descuento": descuento,
                "total": subtotal - descuento,
            }
        except ValueError:
            error = "Ingresa una cantidad entera mayor que cero y un precio no negativo."

    return render_template("compra.html", resultado=resultado, error=error, valores=valores)


@app.route("/salario", methods=["GET", "POST"])
def salario():
    resultado = None
    error = None
    valores = {"horas": "", "pago": ""}

    if request.method == "POST":
        valores = {
            "horas": request.form.get("horas", "").strip(),
            "pago": request.form.get("pago", "").strip(),
        }
        try:
            horas = float(valores["horas"])
            pago = float(valores["pago"])
            if horas < 0 or pago < 0:
                raise ValueError
            horas_normales = min(horas, 40)
            horas_extra = max(horas - 40, 0)
            resultado = {
                "horas": horas,
                "pago": pago,
                "horas_normales": horas_normales,
                "horas_extra": horas_extra,
                "total": horas_normales * pago + horas_extra * pago * 2,
            }
        except ValueError:
            error = "Ingresa horas y pago por hora como números no negativos."

    return render_template("salario.html", resultado=resultado, error=error, valores=valores)


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    resultado = None
    error = None
    celsius = ""

    if request.method == "POST":
        celsius = request.form.get("celsius", "").strip()
        try:
            valor = float(celsius)
            resultado = {
                "celsius": valor,
                "fahrenheit": valor * 9 / 5 + 32,
                "kelvin": valor + 273.15,
            }
        except ValueError:
            error = "Ingresa una temperatura válida en grados Celsius."

    return render_template(
        "temperatura.html", resultado=resultado, error=error, celsius=celsius
    )


@app.route("/empresa")
def empresa():
    return render_template("empresa.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)