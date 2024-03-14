# API de Predicción de Enfermedades de la Piel

Esta API está diseñada para realizar predicciones sobre imágenes de enfermedades de la piel utilizando un modelo de red neuronal previamente entrenado. Permite a los usuarios cargar imágenes y obtener predicciones sobre la enfermedad de la piel que pueda contener la imagen.

## Requisitos

- Python 3.x
- Flask
- TensorFlow
- Flask-CORS
- Waitress
- psutil

## Instalación

1. Clona este repositorio en tu máquina local:


2. Instala las dependencias utilizando pip:

pip install -r requirements.txt

## Uso

1. Ejecuta la aplicación Flask:

python app.py


2. La aplicación estará disponible en `http://localhost:5000`.

### Rutas Disponibles

- `GET /`: Una ruta de prueba para verificar si la API está en funcionamiento. Devuelve un mensaje simple "Hola, mundo!".

- `POST /predict`: Envía una imagen de enfermedad de la piel y devuelve la predicción de la enfermedad detectada, si la confianza es mayor o igual al 0.80. Si la confianza es menor, devuelve un mensaje indicando que no se ha detectado ninguna enfermedad.

- `POST /predict2`: Envía una imagen de enfermedad de la piel y devuelve las predicciones de todas las clases posibles junto con sus respectivas confianzas.

- `POST /img`: Una ruta de prueba para recibir y procesar imágenes. Actualmente, solo devuelve un mensaje indicando que la imagen ha sido recibida y procesada correctamente.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor, sigue los siguientes pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/feature-name`).
3. Realiza tus cambios.
4. Realiza un commit con tus cambios (`git commit -am 'Add new feature'`).
5. Haz push a la rama (`git push origin feature/feature-name`).
6. Crea un nuevo Pull Request.

 
