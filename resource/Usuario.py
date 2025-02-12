from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from model.Usuario import UsuarioModel

class Login(UserMixin, UsuarioModel):
    pass

class UsuarioLogin:
    login = LoginManager()

    @login.user_loader
    def load_user(user_id):
        usuario = UsuarioModel.find_by_id(user_id)
        return usuario



