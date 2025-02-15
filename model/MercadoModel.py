import pandas as pd
from flask import jsonify
from sqlalchemy import Column, Integer, String
from sql import session, Base

class MercadoModel(Base):
    __tablename__ = 'Voos'

    id = Column(Integer, primary_key=True)
    ano = Column(Integer)
    mes = Column(Integer)
    mercado = Column(String)
    rpk = Column(Integer)

    def __init__(self, ano, mes, mercado, rpk):
        self.ano = ano
        self.mes = mes
        self.mercado = mercado
        self.rpk = rpk

    def json(self):
        return {
            "id": self.id,
            "ano": self.ano,
            "mes": self.mes,
            "mercado": self.mercado,
            "rpk": self.rpk
        }

    def find_all():
        voos = []
        for voo in session.query(MercadoModel).all():
            voos.append(voo.json())
        return voos

    def find_by_filters(mercado, mes_inicio, ano_inicio, mes_fim, ano_fim):
        voos = session.query(MercadoModel).filter(
            MercadoModel.mercado.like(f"%{mercado}%")  ,
            MercadoModel.mes >= mes_inicio,
            MercadoModel.ano >= ano_inicio,
            MercadoModel.mes <= mes_fim,
            MercadoModel.ano <= ano_fim
        ).all()

        dados = [{"data" : f"{voo.mes}-{voo.ano}", "rpk": voo.rpk} for voo in voos]

        df = pd.DataFrame(dados)
        df["data"] = pd.to_datetime(df["data"], format="%m-%Y")
        df = df.groupby("data", as_index=False).sum()

        return df


    def find_by_id(id):
        voo = session.query(MercadoModel).get(id)
        return voo.json()

    def find_by_mercado(mercado):
        voos = []
        for voo in session.query(MercadoModel).filter(MercadoModel.mercado.like(f'%{mercado}%')).all():
            voos.append(voo.json())
        return voos

    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            return jsonify({"mensagem" : "Não foi possível salvar o usuario"}), 500




