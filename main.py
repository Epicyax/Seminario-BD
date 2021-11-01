from flask import Flask, jsonify, request
from conexion import crear_usuario, iniciar_sesion
from conexion import insertar_pelicula, get_peliculas, get_pelicula

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods=["POST"])
def usuario():
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

@app.route("/api/v1/peliculas", methods=["GET", "POST"])
@app.route("/api/v1/peliculas/<int:id>", methods=["GET", "POST"])
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