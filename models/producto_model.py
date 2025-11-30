"""
Modelo Producto
-----------------------------------------
Tabla: productos
Representa los productos disponibles en el sistema.
Incluye métodos CRUD básicos.
"""

from core.database import db


class Producto(db.Model):
    __tablename__ = "productos"

    # Campos de la tabla 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)     # Nombre del producto
    descripcion = db.Column(db.String(250))                # Descripción breve
    precio = db.Column(db.Float(11, 2), nullable=False)   # Precio unitario
    stock = db.Column(db.Integer, nullable=False)         # Cantidad disponible

    def __init__(self, nombre, descripcion, precio, stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el producto en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los productos registrados."""
        return Producto.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un producto por ID."""
        return Producto.query.get(id)

    def update(self, nombre=None, descripcion=None, precio=None, stock=None):
        """Actualiza los campos enviados del producto."""
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock
        db.session.commit()

    def delete(self):
        """Elimina el producto de la base de datos."""
        db.session.delete(self)
        db.session.commit()
