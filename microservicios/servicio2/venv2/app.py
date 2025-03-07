from flask import Flask, jsonify
import requests

app2 = Flask(__name__)

@app2.route('/<string:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    try:
        url = f"https://www.el-tiempo.net/api/json/v2/provincias/08/municipios/{municipioid}"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "No se pudo obtener el clima"}), 500
        
        data = response.json()
        
        # Filtrar los datos requeridos
        filtered_data = {
            "temperatura_actual": data.get("temperatura_actual"),
            "temperaturas": {
                "max": data.get("temperaturas", {}).get("max"),
                "min": data.get("temperaturas", {}).get("min")
            },
            "humedad": data.get("humedad"),
            "viento": data.get("viento"),
            "precipitacion": data.get("precipitacion"),
            "lluvia": data.get("lluvia")
        }

        return jsonify(filtered_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app2.run(port=5001, debug=True)