from flask import Flask, jsonify
import requests
app2 = Flask(__name__)


@app2.route('/<string:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):

    try:
        url = f"https://www.el-tiempo.net/api/json/v2/provincias/08/municipios/{municipioid}"
        response = requests.get(url)
       
        #print(jsonify(data))
        if response.status_code != 200:
            return jsonify({"error": "No se pudo obtener el clima"}), 500
        
        data = response.json()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app2.run(port=5001,debug=True)
    