"""
Modelo Cliente
-------------------------------
Representa a los clientes del sistema.
Incluye métodos CRUD básicos.
"""
from core.database import db

class Cliente(db.Model):
    __tablename__ = "clientes"

    # Campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))

    def __init__(self, nombre, email, telefono=None, direccion=None):
        # Constructor: asigna valores iniciales del cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------
    def save(self):
        """Guarda el cliente en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los clientes registrados."""
        return Cliente.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un cliente por su ID."""
        return Cliente.query.get(id)

    def update(self, nombre=None, email=None, telefono=None, direccion=None):
        """Actualiza los campos del cliente solo si se envían."""
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if telefono is not None:
            self.telefono = telefono
        if direccion is not None:
            self.direccion = direccion

        db.session.commit()

    def delete(self):
        """Elimina el cliente de la base de datos."""
        db.session.delete(self)
        db.session.commit()
