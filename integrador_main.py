from coleta_bd import Coleta


from flask import Flask, jsonify, request, make_response

#          INSTANCIANDO O MODULO-->

app =Flask('coleta')

#               Get

@app.route('/coleta',methods=['GET'])
def get_coleta():
    return Coleta

#       VISUALIANDO OS DADOS POR ID -->

@app.route('/coleta/<int:id>', methods=["GET"])
def get_coleta_id(id):
    for coleta in Coleta:
        if coleta.get('id') == id:
         return jsonify(coleta)
        


#     Post -->
@app.route('/coleta', methods=['POST'])
def criar_coleta():
   coleta = request.json
   Coleta.append(coleta)
   return make_response(
      jsonify(mensagem='Coleta de dados registrada com sucesso!!!',
              coleta=coleta)
      
   )

#     EDITANDO DADOS COLETADOS  -->
@app.route('/coleta/<int:id>',methods=['PUT'])
def editar_coleta_id(id):
   coleta_alterada = request.get_json()
   for indice,coleta in enumerate(Coleta):
      if coleta.get('id') == id:
         Coleta[indice].update(coleta_alterada)
         return jsonify(Coleta[indice])
      
# DELETANDO DADOS COLETADOS -->

@app.route('/coleta/<int:id>', methods=['DELETE'])
def excluir_coleta(id):
   for indice,coleta in enumerate(Coleta):
      if coleta.get('id') == id:
         del Coleta[indice]
         return jsonify(mensagem='Os dados da coleta pra o id selecionado foram excluidos',
                        coleta=coleta)


app.run(port=5000, host='localhost')