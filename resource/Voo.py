from flask import jsonify

from model.Voo import VooModel
from flask_restful import Resource

class VooResource(Resource):

    def get(self):
        return {'Voo' : VooModel.find_all()}, 200