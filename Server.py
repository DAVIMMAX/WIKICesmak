# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__)
CORS(app)

@app.route('/save', methods=['POST'])
def save():
    try:
        content = request.get_json()
        conteudo = str(content['conteudo']).encode('utf-8').decode('utf-8')
        logging.info("O conteúdo entrou!")
        with open('conteudo.html', 'w', encoding='utf-8') as f:
            f.write(conteudo)
        return jsonify({'message':'Salvou!'}), 200
    except:
        logging.info(f"O conteúdo NÃO foi salvo com sucesso{request.get_json()}")
        return jsonify({'message':'Erro de Salvamento'}), 500

if __name__ == '__main__':
    app.run(debug=True)