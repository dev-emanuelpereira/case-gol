import csv
from model.MercadoModel import VooModel
from sql import Base, engine

def criar_banco():
    Base.metadata.create_all(bind=engine, checkfirst=True)
    if not VooModel.find_all():
        with open('material/Dados_Estatisticos_tratada_csv.csv', newline='', encoding='UTF-8') as csvfile:
            planilha = csv.reader(csvfile, delimiter=';')
            next(planilha)

            for linha in planilha:
                ano, mes, mercado, rpk = linha
                voo = VooModel(ano, mes, mercado, rpk)

                VooModel.save(voo)
        csvfile.close()
    return

