from model.Voo import VooModel

class VooService:
    def filtrarDados(id=None, mercado=None, ano=None,mes=None):
        if id is not None:
            voo = VooModel.find_by_id(id)
            return voo, 200

        if not VooModel.find_by_filters(mercado, ano, mes):
            return {"mensagem": "Não encontramos dados com o filtro utilizado"}, 404
        voo = VooModel.find_by_filters(mercado, ano, mes)
        return voo, 200