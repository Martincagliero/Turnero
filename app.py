from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Página principal - formulario para reservar
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        fecha = request.form["fecha"]
        hora = request.form["hora"]

        conn = sqlite3.connect("turnos.db")
        c = conn.cursor()
        c.execute("INSERT INTO turnos (nombre, fecha, hora) VALUES (?, ?, ?)", (nombre, fecha, hora))
        conn.commit()
        conn.close()
        return redirect("/")

    # Mostrar los turnos
    conn = sqlite3.connect("turnos.db")
    c = conn.cursor()
    c.execute("SELECT * FROM turnos ORDER BY fecha, hora")
    turnos = c.fetchall()
    conn.close()
    return render_template("index.html", turnos=turnos)

if __name__ == "__main__":
    app.run(debug=True)
