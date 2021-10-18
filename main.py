from flask import Flask, json, jsonify, request
from conexion import crear_usuario

app = Flask(__name__)

@app.route("/api/v1/usuarios", methods=["POST"])
def usuario():
    if request.method == "POST" and request.is_json:
        try:
            data = request.get_json()
            print(data)
            if crear_usuario(data['correo'], data['contrasena']):
                return jsonify({"code":"ok"})
            else:
                return jsonify({"code":"existe"})
        except:
            return jsonify({"code":"error"})

app.run(debug=True)