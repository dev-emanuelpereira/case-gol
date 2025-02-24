import logging

import pandas as pd
from flask import jsonify
from sqlalchemy import Column, Integer, String, and_
from sql import session, Base

class MercadoModel(Base):
    __tablename__ = 'MERCADO'

    id = Column(Integer, primary_key=True)
    empresa_sigla = Column(String)
    ano = Column(Integer)
    mes = Column(Integer)
    mercado = Column(String)
    rpk = Column(Integer)

    def __init__(self, empresa_sigla, ano, mes, mercado, rpk):
        self.empresa_sigla = empresa_sigla
        self.ano = ano
        self.mes = mes
        self.mercado = mercado
        self.rpk = rpk

    def json(self):
        return {
            "id": self.id,
            "empresa_sigla": self.empresa_sigla,
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

    def find_by_filters(empresa_sigla, mercado, mes_inicio, ano_inicio, mes_fim, ano_fim):
        try:
            data_inicio = ano_inicio * 12 + mes_inicio
            data_fim = ano_fim * 12 + mes_fim

            mercados = session.query(MercadoModel).filter(
                MercadoModel.empresa_sigla == empresa_sigla,
                MercadoModel.mercado.like(f"%{mercado}%"),
                and_(
                    (MercadoModel.ano * 12 + MercadoModel.mes) >= data_inicio,
                    (MercadoModel.ano * 12 + MercadoModel.mes) <= data_fim
                )
            ).all()

            dados = [{"data" : f"{mercado.mes}-{mercado.ano}", "rpk": mercado.rpk} for mercado in mercados]

            df = pd.DataFrame(dados)
            df["data"] = pd.to_datetime(df["data"], format="%m-%Y")
            df = df.groupby("data", as_index=False).sum()

            session.close()
        except:
            df = None
        return df


    def find_by_id(id):
        voo = session.query(MercadoModel).get(id)
        session.close()
        return voo.json()

    def find_by_mercado(mercado):
        voos = []
        for voo in session.query(MercadoModel).filter(MercadoModel.mercado.like(f'%{mercado}%')).all():
            voos.append(voo.json())
        session.close()
        return voos

    def save(self):
        try:
            session.add(self)
            session.commit()
            session.close()
        except:
            session.rollback()
            return jsonify({"mensagem" : "Não foi possível salvar o usuario"}), 500




