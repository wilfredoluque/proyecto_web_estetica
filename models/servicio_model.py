"""
Modelo Servicio
-----------------------------------------
Tabla: servicios
Archivo relacionado: servicios_realizados_model.py
Representa los servicios que ofrece el sistema.
"""
from core.database import db

class Servicio(db.Model):
    __tablename__ = "servicios"
    # Campos de la tabla 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)        # Nombre del servicio
    descripcion = db.Column(db.String(250))                   # Descripción breve
    precio = db.Column(db.Float(11, 2), nullable=False)       # Precio del servicio

    # Relación con la tabla 'servicios_realizados'
    # → proviene del modelo ServicioRealizado
    servicios_realizados = db.relationship(
        "ServicioRealizado",
        back_populates="servicio"
    )

    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda un servicio en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los servicios registrados."""
        return Servicio.query.all()

    @staticmethod
    def get_by_id(id):
        """Busca un servicio por ID."""
        return Servicio.query.get(id)

    def update(self, nombre=None, descripcion=None, precio=None):
        """Actualiza los campos enviados."""
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio

        db.session.commit()

    def delete(self):
        """Elimina el servicio de la base de datos."""
        db.session.delete(self)
        db.session.commit()
