"""IMPORTATION DE TOUS LES MODULES NECESSAIRES A L'APPLICATION"""
from flask import Flask, render_template, url_for

app = Flask(__name__)


"""DEFINITION DES ROUTES DE L'APPLICATION"""
@app.route("/")
def welcome():
    return "<h1>Hello</h1>"


"""DEMARRAGE DE L'APPLICATION"""
if __name__ == "__main__":
    app.run()
