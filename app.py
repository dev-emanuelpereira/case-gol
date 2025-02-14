import os
from flask_login import login_required
from sqlalchemy.testing.plugin.plugin_base import logging

from configuration import Config
from flask import Flask
from routes.AuthRoute import AuthRoute
from routes.DashboardRoute import DashboardRoute
from services.AuthService import login_manager

app = Flask(__name__)
login_manager.init_app(app)

app.config['SESSION_PERMANENT'] = False
app.secret_key = os.urandom(24)

app.register_blueprint(DashboardRoute.dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(AuthRoute.auth_bp, url_prefix='/')

if __name__ == '__main__':
    Config.criar_banco()
    app.run(debug=True)

