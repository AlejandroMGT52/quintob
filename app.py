# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola desde mi aplicación Python en Docker y CI!'

if __name__ == '__main__':
    # Usamos 0.0.0.0 para que sea accesible dentro del contenedor Docker
    app.run(debug=True, host='0.0.0.0')