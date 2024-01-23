
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import io
import flask_cors as cors

app = Flask(__name__)
cors.CORS(app)

# Carga el modelo de modelo50
model = tf.keras.models.load_model('skindect_model.h5')
 
 #clases
class_names =['Candidiasis','Eczema','Acne','pigmentacion','benigno','maligno']


@app.route("/",methods=['GET'])
def hello_world():
    return {"message": "Hola, mundo!"}


# Ruta para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    image = request.files['image']
        
    # Convertir objeto FileStorage a objeto io.BytesIO
    image_bytes = io.BytesIO(image.read())

    # Cargar imagen usando io.BytesIO
    image = tf.keras.preprocessing.image.load_img(image_bytes, target_size=(299, 299))

    # Convertir imagen a tensor NumPy
    image = np.array(image)

    # Añadir la dimensión de lote (None)
    image = np.expand_dims(image, axis=0)

    # Hacer predicción
    prediction = model.predict(image)

    # Obtener la clase con mayor probabilidad
    class_index = np.argmax(prediction)

    # Obtener la clase
    class_name = class_names[class_index]

       # Obtener el valor de predicción
    prediction_value = float(prediction[0][class_index])  # Convertir a float

    class_index = int(class_index)
    # Crear un diccionario con la información que deseas devolver
    response_data = {
        'class': class_name,
        'index': class_index,
        'confidence': prediction_value
    }

    # Comprobar si el valor de predicción es mayor al 0.80
    if prediction_value >= 0.80:
        # Devolver el diccionario
        return response_data
    else:
        # Devolver "no se ha detectado ninguna enfermedad"
        return  jsonify({'prediction': 'no se ha detectado ninguna enfermedad'})

@app.route('/predict2', methods=['POST'])
def predict2():
    image = request.files['image']

    # Convertir objeto FileStorage a objeto io.BytesIO
    image_bytes = io.BytesIO(image.read())

    # Cargar imagen usando io.BytesIO
    image = tf.keras.preprocessing.image.load_img(image_bytes, target_size=(224, 224))

    # Convertir imagen a tensor NumPy
    image = np.array(image)

    # Añadir la dimensión de lote (None)
    image = np.expand_dims(image, axis=0)

    # Hacer predicción
    prediction = model.predict(image)

    # Obtener todas las probabilidades de clase
    prediction_values = prediction[0].tolist()  # Convertir a una lista de Python

    # Crear un diccionario con la información que deseas devolver
    response_data = {
        'predictions': [{'class': class_names[i], 'confidence': float(value)} for i, value in enumerate(prediction_values)]
    }

    # Devolver el diccionario con todas las predicciones
    return jsonify(response_data)

@app.route('/img', methods=['POST'])
def vale():
    try:
        # Obtener la imagen del request de Postman
        img_data = request.files.get('image')

        if not img_data:
            return jsonify({'error': 'No image received'}), 400
        
        # Verificar si la imagen es un archivo de imagen válido (por ejemplo, verificar su extensión)
        allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
        if not img_data.filename.lower().split('.')[-1] in allowed_extensions:
            return jsonify({'error': 'Invalid image format'}), 400
        
        # Aquí puedes agregar la lógica para procesar la imagen si es necesario

        return jsonify({'message': 'Image received and processed successfully'}), 200
    
    except ValueError as ve:
        return jsonify({'error': 'Bad Request', 'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
