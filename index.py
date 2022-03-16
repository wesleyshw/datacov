from flask import Flask, render_template
from functions import *


app = Flask(__name__, static_url_path="")


@app.template_filter("to_now")
def format_filter(value):
    return "{0:,}".format(int(value))


@app.route("/")
def index():
    return render_template(
        "index.html",
        dt_updated=dt_updated(),
        regioes=regioes(),
        dados_cov=dados(),
    )


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
