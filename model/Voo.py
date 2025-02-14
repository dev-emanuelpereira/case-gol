import pandas as pd
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

    def find_by_filters(mercado, ano_inicio, ano_fim, mes_inicio, mes_fim):
        # voos = []
        # if not mercado is None:
        #     if not mes is None:
        #         if not ano is None:
        #             for voo in session.query(VooModel).filter(VooModel.mercado.like(f'%{mercado}%')).filter_by(ano=ano, mes=mes).all():
        #                 voos.append(voo.json())
        #             return voos
        #         for voo in session.query(VooModel).filter(VooModel.mercado.like(f'%{mercado}%')).filter_by(mes=mes).all():
        #             voos.append(voo.json())
        #         return voos
        #     for voo in session.query(VooModel).filter(VooModel.mercado.like(f'%{mercado}%')).all():
        #         voos.append(voo.json())
        # else:
        #     VooModel.find_all()
        # return voos

        voos = session.query(VooModel).filter(
            VooModel.mercado.like(f'%{mercado}%'),
            VooModel.ano >= ano_inicio,
            VooModel.ano <= ano_fim,
            VooModel.mes >= mes_inicio if ano_inicio == ano_fim else True,
            VooModel.mes <= mes_fim if mes_inicio == mes_fim else True
        ).all()


        dados = [{"data" : f"{voo.mes}-{voo.ano}", "rpk": voo.rpk} for voo in voos]
        df = pd.DataFrame(dados)
        df["data"] = pd.to_datetime(df["data"], format="%m-%Y")
        df = df.groupby("data", as_index=False).sum()
        return df


    def find_by_id(id):
        voo = session.query(VooModel).get(id)
        return voo.json()

    def find_by_mercado(mercado):
        voos = []
        for voo in session.query(VooModel).filter(VooModel.mercado.like(f'%{mercado}%')).all():
            voos.append(voo.json())
        return voos

    def save(self):
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            return jsonify({"mensagem" : "Não foi possível salvar o usuario"}), 500




