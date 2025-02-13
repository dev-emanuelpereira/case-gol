from datetime import datetime, timedelta

from flask import render_template, Blueprint, request, session, redirect, url_for
from flask_login import current_user, login_required, logout_user
from services.Login import login_manager

from services.Login import criar_usuario, login, login_manager

auth_bp = Blueprint('login', __name__, url_prefix='/login', template_folder='templates')

class Login:
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

    @auth_bp.before_request
    def checar_login():
        if current_user.is_active:
            ultimo_login = session.get('last_activity')
            if ultimo_login:
                ultimo_login = ultimo_login.strptime(ultimo_login, "%Y-%m-%d %H:%M:%S.%f")
                if datetime.now() - ultimo_login > timedelta(minutes=10):
                    logout()
                    return

            session['last_activity'] = datetime.now()
        logout_user()

    @auth_bp.route('/sair', methods=['GET', 'POST'])
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login.login'))

    def sair():
        logout()


    def logout():
        logout_user()