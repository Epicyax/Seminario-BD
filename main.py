from flask import Flask, json, jsonify, request
from conexion import crear_usuario, iniciar_sesion

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