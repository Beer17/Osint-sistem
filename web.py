# osint_web.py

from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Mini OSINT</title>
</head>
<body>
  <h2>Búsqueda OSINT</h2>
  <form method="post">
    <input name="dato" placeholder="Ingresa nombre, IP, etc.">
    <button type="submit">Buscar</button>
  </form>

  {% if resultado %}
    <h3>Resultado:</h3>
    <pre>{{ resultado }}</pre>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        dato = request.form["dato"]
        # Simulación de búsqueda OSINT (puedes reemplazar con llamadas reales a APIs, scraping, etc.)
        resultado = f"🔎 Simulando búsqueda OSINT para: {dato}\n(Agrega lógica real aquí)"
    return render_template_string(TEMPLATE, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
