from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_restful import reqparse
from services.Voo import VooService
voo_bp = Blueprint('voo', __name__, template_folder='templates')

class VooResource:
    @voo_bp.route('/voo')
    def voos():
        return render_template('dashboard.html')


