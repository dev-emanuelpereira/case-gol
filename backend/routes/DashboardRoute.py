import logging
from datetime import datetime, timedelta
from flask import Blueprint, render_template, request, session, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from routes.AuthRoute import AuthRoute
from services.AuthService import login_manager
from services.DashboardService import MercadoService


logging.basicConfig(level=logging.DEBUG)
class DashboardRoute:

    dashboard_bp = Blueprint('dashboard', __name__)
    login_manager.login_view = "authroute.login"
    login_manager.session_protection = "strong"


    @dashboard_bp.route('/')
    @login_required
    def dashboard():
        return render_template("dashboard.html")

    @dashboard_bp.route('/grafico', methods=['GET'])
    @login_required
    def grafico():

            empresa_sigla = request.args.get("empresa_sigla")
            mercado = request.args.get("mercado")
            data_inicio = request.args.get("data_inicio")
            data_fim = request.args.get("data_fim")

            ano_inicio, mes_inicio = map(int, data_inicio.split("-"))
            ano_fim, mes_fim = map(int, data_fim.split("-"))

            dashboard = MercadoService.filtrarDados(
                empresa_sigla=empresa_sigla,
                mercado=mercado,
                mes_inicio=mes_inicio,
                ano_inicio=ano_inicio,
                mes_fim=mes_fim,
                ano_fim=ano_fim
            )

            if dashboard is None:
                logging.warning("Nao foi possivel gerar grafico")
                return {"erro": "Nao foi possivel gerar grafico"}
            else:
                return dashboard


    @dashboard_bp.route('/verificar_sessao')
    def verificar_sessao():
        if not current_user.is_authenticated:
            return jsonify({"error" : "Sessao expirada"}), 401
        return jsonify({"error": "Sessao expirada"}), 200

    @dashboard_bp.before_request
    def checar_login():
        if not current_user.is_authenticated:
            session.clear()
            return

        if current_user.is_authenticated:
            ultimo_login = datetime.strptime(str(session['last_activity']), "%Y-%m-%d %H:%M:%S.%f")
            if datetime.now() - ultimo_login > timedelta(minutes=10):
                AuthRoute.logout()
                session.clear()
                return
            session['last_activity'] = str(datetime.now())






