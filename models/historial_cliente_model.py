"""
Modelo HistorialServicio
-----------------------------------------
Tabla: historial_servicios
Archivos relacionados:
- cliente_model.py (cliente)
- servicio_model.py (servicio)
- usuario_model.py (empleado)
Registra el historial de servicios realizados o cancelados a los clientes,
incluyendo satisfacción y comentarios.
"""
from core.database import db
from datetime import datetime

class HistorialServicio(db.Model):
    __tablename__ = "historial_servicios"
    # Campos de la tabla 'historial_servicios'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)   # Relacionado con Cliente
    servicio_id = db.Column(db.Integer, db.ForeignKey("servicios.id"), nullable=False) # Relacionado con Servicio
    empleado_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=True)   # Relacionado con Usuario
    fecha = db.Column(db.DateTime, default=datetime.now)                               # Fecha del servicio
    estado = db.Column(db.String(50), default="Realizado")                             # Realizado / Cancelado
    satisfaccion = db.Column(db.String(50), default="Bueno")                           # Excelente/Bueno/Regular/Malo
    comentario = db.Column(db.String(500))                                             # Comentarios opcionales

    # Relaciones
    cliente = db.relationship("Cliente")
    servicio = db.relationship("Servicio")
    empleado = db.relationship("Usuario")

    def __init__(self, cliente_id, servicio_id, empleado_id=None, fecha=None,
                estado="Realizado", satisfaccion="Bueno", comentario=""):
        self.cliente_id = cliente_id
        self.servicio_id = servicio_id
        self.empleado_id = empleado_id
        self.fecha = fecha or datetime.now()
        self.estado = estado
        self.satisfaccion = satisfaccion
        self.comentario = comentario

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el registro en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los registros ordenados por fecha descendente."""
        return HistorialServicio.query.order_by(HistorialServicio.fecha.desc()).all()

    @staticmethod
    def get_by_id(id):
        """Busca un historial por ID."""
        return HistorialServicio.query.get(id)

    def update(self, cliente_id=None, servicio_id=None, empleado_id=None,
            fecha=None, estado=None, satisfaccion=None, comentario=None):
        """Actualiza los campos enviados del registro."""
        if cliente_id is not None:
            self.cliente_id = cliente_id
        if servicio_id is not None:
            self.servicio_id = servicio_id
        if empleado_id is not None:
            self.empleado_id = empleado_id
        if fecha is not None:
            self.fecha = fecha
        if estado is not None:
            self.estado = estado
        if satisfaccion is not None:
            self.satisfaccion = satisfaccion
        if comentario is not None:
            self.comentario = comentario
        db.session.commit()

    def delete(self):
        """Elimina el registro de la base de datos."""
        db.session.delete(self)
        db.session.commit()
