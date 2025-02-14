from datetime import datetime, timedelta

from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from flask_login import login_required, current_user

from routes.Auth import Login
from services.Login import login_manager
from services.Voo import VooService
import logging

logging.basicConfig(level=logging.DEBUG)
class VooResource:
    voo_bp = Blueprint('voo', __name__, template_folder='templates')
    login_manager.login_view = "login.login"
    login_manager.session_protection = "strong"


    @voo_bp.route('/')
    @login_required
    def voos():
        return render_template("dashboard.html")

    @voo_bp.route('/grafico', methods=['GET'])
    @login_required
    def grafico():
        try:
            mercado = request.args.get("mercado")
            data_inicio = request.args.get("data_inicio")
            data_fim = request.args.get("data_fim")

            mes_inicio,  ano_inicio= map(int, data_inicio.split("-"))
            mes_fim, ano_fim = map(int, data_fim.split("-"))

            dashboard = VooService.filtrarDados(mercado, ano_inicio, mes_inicio, ano_fim, mes_fim)
        except ValueError as e:
            logging.error(e)
        return dashboard

    @voo_bp.route('/verificar_sessao')
    def verificar_sessao():
        if not current_user.is_authenticated:
            return jsonify({"error" : "Sessao expirada"}), 401
        return jsonify({"error": "Sessao expirada"}), 200

    @voo_bp.before_request
    def checar_login():
        if not current_user.is_authenticated:
            session.clear()
            return

        if current_user.is_authenticated:
            ultimo_login = datetime.strptime(str(session['last_activity']), "%Y-%m-%d %H:%M:%S.%f")
            if datetime.now() - ultimo_login > timedelta(seconds=10):
                Login.logout()
                session.clear()
                return
            session['last_activity'] = str(datetime.now())






