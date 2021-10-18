from flask import Flask, jsonify
from conexion import get_usuarios

app = Flask(__name__)


@app.route("/")
def hola():
    return "<b>Hola Mundo!<b>"


@app.route("/api/v1/usuarios")
def usuarios():
    usuarios_list = get_usuarios()
    return jsonify(usuarios_list)


app.run()