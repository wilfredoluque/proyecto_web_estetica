"""
Modelo Productividad
-----------------------------------------
Tabla: productividad
Archivo relacionado: usuario_model.py (empleado)
Registra la productividad de cada empleado por día.
Incluye clientes atendidos, ventas y horas trabajadas.
"""
from core.database import db
from datetime import datetime

class Productividad(db.Model):
    __tablename__ = "productividad"

    # Campos de la tabla 'productividad'
    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)  # Relacionado con Usuario
    fecha = db.Column(db.Date, nullable=False, default=datetime.now)                   # Fecha del registro
    clientes_atendidos = db.Column(db.Integer, default=0)                                # Número de clientes atendidos
    ventas_realizadas = db.Column(db.Float, default=0.0)                                 # Total de ventas
    horas_trabajadas = db.Column(db.Float, default=0.0)                                  # Horas trabajadas
    observacion = db.Column(db.String(500))                                              # Comentarios u observaciones

    # Relación con empleado (Usuario)
    empleado = db.relationship("Usuario")

    def __init__(self, empleado_id, fecha, clientes_atendidos=0, ventas_realizadas=0,
                horas_trabajadas=0, observacion=""):
        self.empleado_id = empleado_id
        self.fecha = fecha
        self.clientes_atendidos = clientes_atendidos
        self.ventas_realizadas = ventas_realizadas
        self.horas_trabajadas = horas_trabajadas
        self.observacion = observacion

    # -----------------------
    # MÉTODOS CRUD
    # -----------------------

    def save(self):
        """Guarda el registro de productividad en la base de datos."""
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Retorna todos los registros de productividad, ordenados por fecha descendente."""
        return Productividad.query.order_by(Productividad.fecha.desc()).all()

    @staticmethod
    def get_by_id(id):
        """Busca un registro de productividad por ID."""
        return Productividad.query.get(id)

    def update(self, empleado_id=None, fecha=None, clientes_atendidos=None,
                ventas_realizadas=None, horas_trabajadas=None, observacion=None):
        """Actualiza los campos enviados del registro."""
        if empleado_id is not None:
            self.empleado_id = empleado_id
        if fecha is not None:
            self.fecha = fecha
        if clientes_atendidos is not None:
            self.clientes_atendidos = clientes_atendidos
        if ventas_realizadas is not None:
            self.ventas_realizadas = ventas_realizadas
        if horas_trabajadas is not None:
            self.horas_trabajadas = horas_trabajadas
        if observacion is not None:
            self.observacion = observacion
        db.session.commit()

    def delete(self):
        """Elimina el registro de la base de datos."""
        db.session.delete(self)
        db.session.commit()
