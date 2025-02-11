from flask import jsonify
from sqlalchemy import Column, Integer, String

from sql import session, Base


class VooModel(Base):
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
        for voo in session.query(VooModel).all():
            voos.append(voo.json())
        return voos

    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            return jsonify({"mensagem" : "Não foi possível salvar o usuario"}), 500




