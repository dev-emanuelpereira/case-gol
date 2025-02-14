import os
from flask_login import login_required
from sqlalchemy.testing.plugin.plugin_base import logging

from configuration import config
from flask import Flask
from routes.Auth import Login
from routes.Voo import VooResource
from services.Login import login_manager

app = Flask(__name__)
login_manager.init_app(app)

app.config['SESSION_PERMANENT'] = False
app.secret_key = os.urandom(24)

app.register_blueprint(VooResource.voo_bp, url_prefix='/voo')
app.register_blueprint(Login.auth_bp, url_prefix='/')



if __name__ == '__main__':
    config.criar_banco()
    app.run(debug=True)

