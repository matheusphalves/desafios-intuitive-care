import json
import jsonpickle
from flask import Flask, request, jsonify
from flask_cors import CORS
from domain.queryService import QueryService

#criada instancia da classe
app = Flask(__name__)
CORS(app)
qS = QueryService()
qS.readCSV(filePath='resources/Relatorio_cadop.csv')
#-----------INTERAÇÃO COM O FRONT
#classificar novamente se necessário
@app.route("/query_items", methods = ['POST'])
def queryItems():
    content = request.json
    result = qS.searchItems(content['query'])
    if(len(result)>0):
        toSend = [jsonpickle.encode(item.__dict__) for item in result]
        response = jsonify(toSend)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return jsonify(success=False)

#-----------APLICAÇÃO DISPONÍVEL NA PORTA 5100
app.run(port=5100) #aplicação disponível na porta: 5100, ip: localhost