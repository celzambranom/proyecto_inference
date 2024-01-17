from flask import Flask, render_template, request
import requests
import base64
import json

app = Flask(__name__)

#Cargar configuraciones de config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)
# Obtener valores de configuración
api_url_server = config.get("url_server")
flask_port = config.get("flask_port_front")

@app.route('/')
def index():
    return render_template('hola.html')

@app.route('/clasificar_imagen', methods=['POST'])
def clasificar_imagen():
    # Obtener el tipo de modelo seleccionado del formulario
    tipo_modelo = request.form.get('modelo')

    # Obtener el la imagen desde archivo
    if 'imagen' in request.files:
        image_file = request.files['imagen']
        image_data = image_file.read()

    # Reemplaza 'base64_encoded_image_data' con los datos reales de tu imagen en base64
    imagen_base64 = base64.b64encode(image_data).decode('utf-8')

    # Define el JSON con la imagen en base64
    data = {'imagen_base64': imagen_base64, 'tipo_modelo': tipo_modelo}

        # Envía la imagen a la segunda aplicación
    response = requests.post(api_url_server, json={'imagen_base64': data['imagen_base64'], 'tipo_modelo': data['tipo_modelo']})

    respuestas = response.json()
    salidas=respuestas['predictions']
    model=respuestas['model']
    # Imprime la respuesta
    print(salidas)
    return render_template('hola.html', salidas=salidas, model=model)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=flask_port)