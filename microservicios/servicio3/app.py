from flask import Flask, jsonify
import json

app3 = Flask(__name__)

def cargar_datos():
    with open('venv3/demo.json', 'r', encoding='utd-8') as file:
        return json.load(file)

@app3.route('/<string:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):

    datos = cargar_datos()

    if datos.get("municipioid") == municipioid:
        return jsonify(datos)
    else:
        return jsonify({"error"})
    
if __name__ == '__main__':
    app3.run(port=5002)