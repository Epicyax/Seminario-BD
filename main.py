from flask import Flask, json, jsonify, request
from conexion import crear_usuario, iniciar_sesion
from conexion import insertar_pelicula, get_peliculas, get_pelicula
from conexion import modificar_pelicula, eliminar_pelicula
from conexion import get_peliculas_usuario

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods=["POST"])
@app.route("/api/v1/usuarios/<int:id>/peliculas", methods=["GET"])
def usuario(id=None):
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if crear_usuario(data['correo'], data['contrasena']):
                return jsonify({"code":"Ok"})
            else:
                return jsonify({"code":"Existe"})
        except:
            return jsonify({"code":"Error"})
    elif request.method == "GET" and id is not None:
        return jsonify(get_peliculas_usuario(id))


@app.route("/api/v1/peliculas", methods=["GET", "POST"])
@app.route("/api/v1/peliculas/<int:id>", methods=["GET", "PATCH", "DELETE"])
def peliculas(id=None):
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if insertar_pelicula(data):
                return jsonify({"code":"ok"})
            else:
                return jsonify({"code":"no"})
        except:
            return jsonify({"code":"error"})
    elif request.method == "GET" and id is None:
        return jsonify(get_peliculas())
    elif request.method == "GET" and id is not None:
        return jsonify(get_pelicula(id))
    elif request.method == "PATCH" and id is not None and request.is_json:
        data = request.get_json()
        columna = data['columna']
        valor = data['valor']

        if modificar_pelicula(id, columna, valor):
            return jsonify(code='ok')
        else:
            return jsonify(code='error')
    elif request.method == "DELETE" and id is not None:
        if eliminar_pelicula(id):
            return jsonify(code='ok')
        else:
            return jsonify(code='error')


@app.route("/api/v1/sesiones", methods=["POST"])
def sesion():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            correo = data['correo']
            contrasena = data['contrasena']
            id, ok = iniciar_sesion(correo, contrasena)
            if ok:
                return jsonify({"code": "Ok", "id": id})
            else:
                return jsonify({"code": "No existe"})
        except:
            return jsonify({"code":"Error"})

app.run(debug=True)