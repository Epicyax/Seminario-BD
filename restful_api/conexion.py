import mysql.connector

bd = mysql.connector.connect(
    user = 'emmanuel', password = '12345',
    database = 'cinemapp')

cursor = bd.cursor()

def get_usuarios():
    consulta = "SELECT * FROM usuario"

    cursor.execute(consulta)
    usuarios = []
    for row in cursor.fetchall():
        usuario = {
            'id': row[0],
            'correo': row[1],
            'contrasena': row[2]
        }
        usuarios.append(usuario)
    return usuarios