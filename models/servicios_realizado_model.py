"""
Modelo ServicioRealizado
------------------------------------------
Registra los servicios realizados a clientes.
Incluye relaciones con Cliente y Servicio,
además de métodos CRUD.
"""

from core.database import db
from models.servicio_model import Servicio
from models.cliente_model import Cliente


class ServicioRealizado(db.Model):
    __tablename__ = "servicios_realizados"

    # Campos de la tabla
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    servicio_id = db.Column(db.Integer, db.ForeignKey("servicios.id"))
    fecha = db.Column(db.DateTime, nullable=False)
    precio = db.Column(db.Float(11, 2), nullable=False)

    # Relaciones con otras tablas
    cliente = db.relationship("Cliente")
    servicio = db.relationship("Servicio", back_populates="servicios_realizados")

    def __init__(self, cliente_id, servicio_id, fecha, precio):
        # Constructor: asigna valores del servicio realizado
        self.cliente_id = cliente_id
        self.servicio_id = servicio_id
        self.fecha = fecha
        self.precio = precio

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el registro en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los servicios realizados."""
        return ServicioRealizado.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un servicio realizado por su ID."""
        return ServicioRealizado.query.get(id)

    def update(self, cliente_id=None, servicio_id=None, fecha=None, precio=None):
        """Actualiza campos enviados del registro."""
        if cliente_id:
            self.cliente_id = cliente_id
        if servicio_id:
            self.servicio_id = servicio_id
        if fecha:
            self.fecha = fecha
        if precio is not None:
            self.precio = precio

        db.session.commit()

    def delete(self):
        """Elimina el registro de la base de datos."""
        db.session.delete(self)
        db.session.commit()
