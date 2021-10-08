from flask import Flask, request, jsonify
from service.queryService import QueryService

#criada instancia da classe
app = Flask(__name__)
qS = QueryService()
qS.readCSV(filePath='resources/Relatorio_cadop.csv')
#-----------INTERAÇÃO COM O FRONT
#classificar novamente se necessário
@app.route("/query_items", methods = ['POST'])
def queryItems():
    content = request.json
    result = qS.searchItems(content['query'])
    if(len(result)>0):
        return jsonify(result)
    return jsonify(success=False)

#-----------APLICAÇÃO DISPONÍVEL NA PORTA 5100
app.run(port=5100) #aplicação disponível na porta: 5100, ip: localhost