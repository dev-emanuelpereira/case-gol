from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, login_required


import sql
from model.Usuario import UsuarioModel

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    print(f"Debug: user_id recebido no load_user: {user_id}")
    if not user_id:
        return None
    return UsuarioModel.find_by_id(user_id)



def login(username, password):
    usuario = UsuarioModel.find_by_usuario(username)
    if usuario and usuario.getSenha(password):
        login_user(usuario)
        usuario.ultimoLogin = datetime.now()
        sql.session.commit()
        return True
    return False

def criar_usuario(primNome, username, password):
    usuario = UsuarioModel(primNome, username, password)
    usuario.salvarUsuario()








