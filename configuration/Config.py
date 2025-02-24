import csv
from model.MercadoModel import MercadoModel
from sql import Base, engine

def criar_banco():

    if not MercadoModel.find_all():
        with open('material/Dados_Estatisticos_tratada_csv.csv', newline='', encoding='UTF-8') as csvfile:
            planilha = csv.reader(csvfile, delimiter=';')
            next(planilha)

            for linha in planilha:
                ano, mes, mercado, rpk = linha
                voo = MercadoModel(ano, mes, mercado, rpk)

                MercadoModel.save(voo)
        csvfile.close()
    return

