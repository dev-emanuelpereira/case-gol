from flask import render_template, Blueprint, request, session, redirect, url_for, flash
from flask_login import current_user
from services.AuthService import criar_usuario, login, sair
from datetime import datetime, timedelta
import logging
from services.DashboardService import MercadoService


class AuthRoute:

    auth_bp = Blueprint('authroute', __name__, url_prefix='/login')

    @auth_bp.route('/', methods=['GET', 'POST'])
    @auth_bp.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']

            check = login(username, password)
            if check:
                return redirect(url_for('dashboard.dashboard'))
            flash("Usuario ou senha incorretos.")
        return render_template('index.html')

    @auth_bp.route('/criar-conta', methods=['GET', 'POST'])
    def criar_conta():
        if request.method == 'POST':
            primNome = request.form['primNome']
            username = request.form['usuario']
            password = request.form['password']

            novo_usuario = criar_usuario(primNome, username, password)
            if not novo_usuario:
                flash("Este usuario já existe.")
                return redirect(url_for('authroute.criar_conta'))

            return redirect(url_for('authroute.login'))

        return render_template('cadastro.html')

    @auth_bp.route('/sair', methods=['POST'])
    def logout():
        sair()
        session.clear()
        return redirect(url_for('authroute.login'))
