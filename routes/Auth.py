from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import current_user

from services.Login import criar_usuario, login, sair
from datetime import datetime, timedelta
class Login:

    auth_bp = Blueprint('login', __name__, url_prefix='/login', template_folder='templates')

    @auth_bp.route('/login/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['usuario']
            password = request.form['password']

            check = login(username, password)
            if check:
                return redirect(url_for('voo.voos'))
        return render_template('auth.html')

    @auth_bp.route('/criar-conta', methods=['GET', 'POST'])
    def criar_conta():
        if request.method == 'POST':
            primNome = request.form['primNome']
            username = request.form['usuario']
            password = request.form['password']

            criar_usuario(primNome, username, password)
            return redirect(url_for('login.login'))

        return render_template('criarConta.html')

    @auth_bp.route('/sair', methods=['POST'])
    def logout():
        sair()
        session.clear()
        return redirect(url_for('login.login'))

    @auth_bp.before_request
    def checar_login():
        if not current_user.is_authenticated:
            session.clear()
            return

        if current_user.is_authenticated:
            ultimo_login = str(datetime.now())
            if datetime.now() - ultimo_login > timedelta(seconds=10):
                Login.logout()
                session.clear()
                return
            session['last_activity'] = str(datetime.now())