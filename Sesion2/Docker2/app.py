from flask import Flask

# Crear la instancia o clase Flask
app = Flask(__name__)

# Ruta Servicio
@app.route('/api/hello')
def hello():
    """
        Get hello
        Retorna un mensaje de conexion
    """
    return "Hola Mundo desde Docker"

# Ruta de obtener data
@app.route('/api/getData')
def getData():
    """
        Get Data
        Retorna un dato particular
    """
    resultado = "Data Obtenida"
    return resultado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)