from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import current_user
from services.AuthService import criar_usuario, login, sair
from datetime import datetime, timedelta

from services.DashboardService import MercadoService


class AuthRoute:

    auth_bp = Blueprint('authroute', __name__, url_prefix='/login', template_folder='templates', static_folder='static')

    @auth_bp.route('/', methods=['GET', 'POST'])
    @auth_bp.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']

            check = login(username, password)
            if check:
                return redirect(url_for('dashboard.dashboard'))
        return render_template('auth.html')

    @auth_bp.route('/criar-conta', methods=['GET', 'POST'])
    def criar_conta():
        if request.method == 'POST':
            primNome = request.form['primNome']
            username = request.form['usuario']
            password = request.form['password']

            criar_usuario(primNome, username, password)
            return redirect(url_for('authroute.login'))

        return render_template('criarConta.html')

    @auth_bp.route('/sair', methods=['POST'])
    def logout():
        sair()
        session.clear()
        return redirect(url_for('authroute.login'))
