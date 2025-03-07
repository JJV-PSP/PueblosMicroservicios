from flask import Flask, jsonify
import json

app1 = Flask(__name__)

def cargar_datos():
    with open('municipio.json', 'r', encoding='utf-8') as file:
        return json.load(file)  

@app1.route('/<string:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    datos = cargar_datos()

    if datos.get("municipioid") == municipioid:
        return jsonify(datos)
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404

if __name__ == '__main__':
    app1.run(host='0.0.0.0', port=5000)

