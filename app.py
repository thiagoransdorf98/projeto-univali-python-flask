from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    """Exibe a documentação principal do projeto."""
    return render_template("index.html")


if __name__ == "__main__":
    # Servidor de desenvolvimento: não usar assim em produção.
    app.run(debug=True)
