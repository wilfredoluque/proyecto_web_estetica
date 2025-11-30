"""
Modelo Usuario
-----------------------------------
Representa a los usuarios del sistema.
Incluye autenticación y métodos CRUD.
"""

from core.database import db
from config.security import hash_password, verify_password


class Usuario(db.Model):
    __tablename__ = "usuarios"

    # Campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), default="empleado")

    def __init__(self, nombre, email, password, rol="empleado"):
        # Se encripta la contraseña antes de guardarla
        self.nombre = nombre
        self.email = email
        self.password = hash_password(password)
        self.rol = rol

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el usuario en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los usuarios."""
        return Usuario.query.all()

    @staticmethod
    def get_by_id(id):
        """Obtiene un usuario por ID."""
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        """Busca un usuario por su correo."""
        return Usuario.query.filter_by(email=email).first()

    def update(self, nombre=None, email=None, rol=None, password=None):
        """Actualiza solo los campos enviados."""
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if rol:
            self.rol = rol
        if password:
            self.password = hash_password(password)

        db.session.commit()

    def delete(self):
        """Elimina el usuario de la base de datos."""
        db.session.delete(self)
        db.session.commit()

    # -----------------------
    # AUTENTICACIÓN
    # -----------------------

    def check_password(self, password):
        """Verifica si la contraseña ingresada es correcta."""
        return verify_password(self.password, password)
