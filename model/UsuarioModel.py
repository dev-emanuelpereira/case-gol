import hashlib
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Integer, Column, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from sql import Base, session

class UsuarioModel(Base, UserMixin):

    __tablename__ = 'Usuarios'

    id = Column(Integer, primary_key=True)
    primNome = Column(String, nullable=False)
    usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    ultimoLogin = Column(DateTime)

    def __init__(self, primNome, usuario, senha):
        self.primNome = primNome
        self.usuario = usuario
        self.senha = senha

    def getSenha(self, senha):
        return check_password_hash(self.senha, senha)

    def setSenha(self, senha):
        self.senha = generate_password_hash(senha)

    def getUsuario(usuario):
        return hashlib.sha256(usuario.encode()).hexdigest()

    def setUsuario(self, usuario):
        self.usuario = hashlib.sha256(usuario.encode()).hexdigest()

    def salvarUltimoLogin(self):
        session.add(self.ultimoLogin)
        session.commit()

    def salvarUsuario(self):
        try:
            self.setUsuario(self.usuario)
            self.setSenha(self.senha)
            self.ultimoLogin = datetime.now()
            session.add(self)
            session.commit()
        except:
            session.rollback()

    def salvarUltimoLogin(self):
        try:
            session.add(UsuarioModel.ultimoLogin)
            session.commit()
        except:
            session.rollback()

    def find_by_id(id):
        return session.query(UsuarioModel).filter_by(id=id).first()

    def find_by_usuario(usuario):
        username = UsuarioModel.getUsuario(usuario)
        usuario = session.query(UsuarioModel).filter_by(usuario = username).first()
        return usuario


