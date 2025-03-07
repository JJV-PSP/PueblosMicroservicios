from flask import Flask, jsonify
import requests

app4 = Flask(__name__)

@app4.route('/<string:municipioid>/<string:parametro1>/<string:parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    parametros = {parametro1, parametro2}

    json_final = {}

    if "geo" in parametros:
        # Antes iba al localhost en vez de al nombre de servicio. Se ha puesto así para probar a conectar al desplegar
        url = f"http://servicio1:5000/{municipioid}/geo"
        response = requests.get(url)
        if response.status_code == 200:
            json_final["Datos geográficos"] = response.json()
        else:
            json_final["Datos geográficos"] = {"error": "No se pudieron obtener los datos del municipio."}

    if "meteo" in parametros:
        # Antes iba al localhost en vez de al nombre de servicio. Se ha puesto así para probar a conectar al desplegar
        url = f"http://servicio2:5001/{municipioid}/meteo"
        response = requests.get(url)
        if response.status_code == 200:
            json_final["Datos meteorológicos"] = response.json()
        else:
            json_final["Datos meteorológicos"] = {"error": "No se pudo obtener el clima."}

    if "demo" in parametros:
        # Antes iba al localhost en vez de al nombre de servicio. Se ha puesto así para probar a conectar al desplegar
        url = f"http://servicio3:5002/{municipioid}/demo"
        response = requests.get(url)
        if response.status_code == 200:
            json_final["Datos demográficos"] = response.json()
        else:
            json_final["Datos demográficos"] = {"error": "No se pudieron obtener los datos demográficos."}

    return jsonify(json_final)

if __name__ == '__main__':
    app4.run(host='0.0.0.0', port=5003, debug=True)