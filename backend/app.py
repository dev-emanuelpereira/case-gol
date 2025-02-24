import logging
import os
from datetime import datetime
from configuration import Config
from flask import Flask, request
from routes.AuthRoute import AuthRoute
from routes.DashboardRoute import DashboardRoute
from services.AuthService import login_manager


data_atual = datetime.now()
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

log_filename = os.path.join(log_dir, f"aplicacao_{data_atual.year}-{data_atual.month:02d}-{data_atual.day:02d}.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
login_manager.init_app(app)

app.config['SESSION_PERMANENT'] = False
app.secret_key = os.urandom(24)

app.register_blueprint(DashboardRoute.dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(AuthRoute.auth_bp, url_prefix='/')

@app.before_request
def salvar_logs():
    logging.info(f"{request.remote_addr} - {request.method} {request.path}")
    logging.getLogger().handlers[0].flush()

if __name__ == '__main__':
    #Config.criar_banco()
    app.run(host="0.0.0.0", port=5000, debug=True)

