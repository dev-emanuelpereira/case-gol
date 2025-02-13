from flask import jsonify
from model.Voo import VooModel
from flask_restful import Resource, reqparse

body = reqparse.RequestParser()
body.add_argument('id', type=int, required=False)
body.add_argument('mercado', type=str, required=False)
body.add_argument('ano', type=int, required=False)
body.add_argument('mes', type=int, required=False)

class VooService:
    def filtrarDados():
        dados = body.parse_args()
        if dados['id']:
            voo = VooModel.find_by_id(dados['id'])
            return voo, 200

        if not VooModel.find_by_filters(dados['mercado'], dados['ano'], dados['mes']):
            return {"mensagem" : "Não encontramos dados com o filtro utilizado"}, 404
        voo = VooModel.find_by_filters(dados['mercado'], dados['ano'], dados['mes'])
        return voo, 200


