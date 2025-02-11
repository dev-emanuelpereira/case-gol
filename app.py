import csv

from flask import Flask
from flask_restful import Api

from model.Voo import VooModel
from sql import Base, engine
from resource.Voo import VooResource

app = Flask(__name__)
api = Api(app)

#@app.before_request
# routes_voo():
api.add_resource(VooResource, '/voo', methods=['GET'])

@app.before_request
def criar_banco():
    Base.metadata.create_all(bind=engine)
    if not VooModel.find_all():
        with open('material/Dados_Estatisticos_tratada_csv.csv', newline='', encoding='UTF-8') as csvfile:
            planilha = csv.reader(csvfile, delimiter=';')
            next(planilha)

            for linha in planilha:
                ano, mes, mercado, rpk = linha
                voo = VooModel(ano, mes, mercado, rpk)

                VooModel.save(voo)

if __name__ == '__main__':
    app.run(debug=True)

