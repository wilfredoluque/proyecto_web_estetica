"""
Modelo Inventario
-----------------------------------------
Tabla: inventario
Archivo relacionado: producto_model.py
Registra la cantidad y ubicación de cada producto en stock.
"""

from core.database import db
from models.producto_model import Producto


class Inventario(db.Model):
    __tablename__ = "inventario"

    # Campos de la tabla 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))  # Relacionado con Producto
    cantidad = db.Column(db.Integer, nullable=False)                     # Cantidad disponible
    ubicacion = db.Column(db.String(100))                                 # Ubicación en almacén

    # Relación con producto
    producto = db.relationship("Producto")

    def __init__(self, producto_id, cantidad, ubicacion=""):
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.ubicacion = ubicacion

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el registro de inventario en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los registros de inventario."""
        return Inventario.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un registro de inventario por ID."""
        return Inventario.query.get(id)

    def update(self, producto_id=None, cantidad=None, ubicacion=None):
        """Actualiza los campos enviados del registro de inventario."""
        if producto_id:
            self.producto_id = producto_id
        if cantidad is not None:
            self.cantidad = cantidad
        if ubicacion is not None:
            self.ubicacion = ubicacion
        db.session.commit()

    def delete(self):
        """Elimina el registro de inventario de la base de datos."""
        db.session.delete(self)
        db.session.commit()
