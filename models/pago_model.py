"""
Modelo Pago
-----------------------------------------
Tabla: pagos
Archivo relacionado: cliente_model.py
Registra los pagos realizados por los clientes.
Incluye monto, fecha y descripción opcional.
"""

from core.database import db
from models.cliente_model import Cliente


class Pago(db.Model):
    __tablename__ = "pagos"

    # Campos de la tabla 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))  # Relacionado con Cliente
    fecha = db.Column(db.DateTime, nullable=False)                     # Fecha del pago
    monto = db.Column(db.Float(11, 2), nullable=False)                # Monto pagado
    descripcion = db.Column(db.String(250))                             # Descripción opcional

    # Relación con cliente
    cliente = db.relationship("Cliente")

    def __init__(self, cliente_id, fecha, monto, descripcion=""):
        self.cliente_id = cliente_id
        self.fecha = fecha
        self.monto = monto
        self.descripcion = descripcion

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el pago en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los pagos registrados."""
        return Pago.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un pago por ID."""
        return Pago.query.get(id)

    def update(self, cliente_id=None, fecha=None, monto=None, descripcion=None):
        """Actualiza los campos enviados del pago."""
        if cliente_id:
            self.cliente_id = cliente_id
        if fecha:
            self.fecha = fecha
        if monto is not None:
            self.monto = monto
        if descripcion is not None:
            self.descripcion = descripcion
        db.session.commit()

    def delete(self):
        """Elimina el pago de la base de datos."""
        db.session.delete(self)
        db.session.commit()
