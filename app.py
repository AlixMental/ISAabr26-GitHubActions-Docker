from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Definimos las variables de tu perfil
    nombre = "Fernando"
    rol = "Programador y Modelador 3D"
    
    # Pasamos ambas variables al HTML
    return render_template('index.html', nombre=nombre, rol=rol)

if __name__ == '__main__':
    # Ejecutar en el puerto 5000
    app.run(host='0.0.0.0', debug=True, port=5000)