from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ruta del directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))

# Ruta completa al archivo skindect_model.h5
skindect_model_path = os.path.join(current_directory, 'skindect_model.h5')

@app.route("/", methods=['GET'])
def hello_world():
    return {"message": "Hola, mundo!", "skindect_model_path": skindect_model_path}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
