import csv
import os
from datetime import timedelta

from flask import Flask
from routes.Auth import auth_bp
from routes.Voo import voo_bp
from model.Voo import VooModel
from services.Login import login_manager
from sql import Base, engine


app = Flask(__name__)
login_manager.init_app(app)
app.register_blueprint(voo_bp, url_prefix='/voo')
app.register_blueprint(auth_bp, url_prefix='/')
app.secret_key = os.urandom(24)

#Criar base
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

