import cv2
import numpy as np
from skimage import color, feature
import json

def calcular_textura_piel(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    textura = feature.graycomatrix(gris, [5], [0], symmetric=True, normed=True)
    textura_promedio = np.mean(textura)
    return textura_promedio

def calcular_color_piel(imagen):
    lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)
    color_promedio = np.mean(lab, axis=(0, 1))
    return color_promedio.tolist()

def calcular_hidratacion(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    suavizado = cv2.GaussianBlur(gris, (15, 15), 0)
    gradiente = cv2.Laplacian(suavizado, cv2.CV_64F).var()
    hidratacion = 100 - gradiente
    return hidratacion

def calcular_arrugas(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(gris, 50, 150)
    cantidad_arrugas = np.sum(bordes) / 255
    return cantidad_arrugas

def calcular_exposicion_solar(imagen):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    exposicion_solar = np.sum(gris > 200) / gris.size * 100
    return exposicion_solar

def interpretar_resultados(resultados):
    interpretacion = {
        "textura_piel": "Suave" if resultados["textura_piel"] < 0.0001 else "Irregular",
        "color_piel": "Normal" if all(150 < c < 180 for c in resultados["color_piel"]) else "Fuera de lo comun",
        "hidratacion": "Alta" if resultados["hidratacion"] > 95 else "Baja",
        "arrugas": "Pocas" if resultados["arrugas"] < 5000 else "Muchas",
        "exposicion_solar": "Baja" if resultados["exposicion_solar"] < 10 else "Alta"
    }
    return interpretacion

def obtener_caracteristicas_piel(imagen_path):
    imagen = cv2.imread(imagen_path)
    
    textura_piel = calcular_textura_piel(imagen)
    color_piel = calcular_color_piel(imagen)
    hidratacion = calcular_hidratacion(imagen)
    arrugas = calcular_arrugas(imagen)
    exposicion_solar = calcular_exposicion_solar(imagen)

    caracteristicas = {
        "textura_piel": textura_piel,
        "color_piel": color_piel,
        "hidratacion": hidratacion,
        "arrugas": arrugas,
        "exposicion_solar": exposicion_solar
    }

    interpretacion = interpretar_resultados(caracteristicas)
    return json.dumps(interpretacion, indent=4)

# Ruta de la imagen que deseas analizar
ruta_imagen = 'rostro2.jpg'

# Obtener características de la piel y mostrar como JSON
resultados = obtener_caracteristicas_piel(ruta_imagen)
print(resultados)
