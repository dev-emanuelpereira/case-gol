from sqlalchemy import Integer, Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from sql import Base, session


class UsuarioModel(Base):

    id = Column(Integer, primary_key=True)
    usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def salvar_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def checar_senha(self, senha):
        return check_password_hash(senha)

    def find_by_id(id):
        usuario = session.query(UsuarioModel).filter_by(id = id).first()
        return usuario