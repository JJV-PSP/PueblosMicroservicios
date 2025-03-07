from flask import Flask, jsonify
import json

app3 = Flask(__name__)

def cargar_datos():
    with open('demo.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app3.route('/<string:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):

    datos = cargar_datos()

    if datos.get("municipioid") == municipioid:
        return jsonify(datos)
    else:
        return jsonify({"error":"Datos demográficos no encontrados."})
    
if __name__ == '__main__':
    app3.run(host='0.0.0.0', port=5002)