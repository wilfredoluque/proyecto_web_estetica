"""
Modelo Reserva
-----------------------------------------
Tabla: reservas
Archivos relacionados:
- cliente_model.py (cliente)
- servicio_model.py (servicio)
- usuario_model.py (empleado)
Registra las reservas de servicios realizadas por los clientes.
"""

from core.database import db
from models.cliente_model import Cliente
from models.usuario_model import Usuario
from models.servicio_model import Servicio
from datetime import datetime


class Reserva(db.Model):
    __tablename__ = "reservas"

    # Campos de la tabla 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))   # Relacionado con Cliente
    servicio_id = db.Column(db.Integer, db.ForeignKey("servicios.id")) # Relacionado con Servicio
    empleado_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))  # Relacionado con Usuario
    fecha = db.Column(db.DateTime, nullable=False)                     # Fecha de la reserva
    estado = db.Column(db.String(50), default="Pendiente")             # Estado actual

    # Relaciones con otros modelos
    cliente = db.relationship("Cliente")
    servicio = db.relationship("Servicio")
    empleado = db.relationship("Usuario")

    def __init__(self, cliente_id, servicio_id, empleado_id, fecha, estado="Pendiente"):
        self.cliente_id = cliente_id
        self.servicio_id = servicio_id
        self.empleado_id = empleado_id
        self.fecha = fecha
        self.estado = estado

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda la reserva en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todas las reservas."""
        return Reserva.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca una reserva por ID."""
        return Reserva.query.get(id)

    def update(self, cliente_id=None, servicio_id=None, empleado_id=None, fecha=None, estado=None):
        """Actualiza los campos enviados de la reserva."""
        if cliente_id:
            self.cliente_id = cliente_id
        if servicio_id:
            self.servicio_id = servicio_id
        if empleado_id:
            self.empleado_id = empleado_id
        if fecha:
            self.fecha = fecha
        if estado:
            self.estado = estado
        db.session.commit()

    def delete(self):
        """Elimina la reserva de la base de datos."""
        db.session.delete(self)
        db.session.commit()
