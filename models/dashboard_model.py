"""
Modelo Dashboard
-----------------------------------------
Archivo relacionado: 
- cliente_model.py (Clientes)
- servicios_realizado_model.py (Servicios realizados)
- pago_model.py (Pagos/Ingresos)
- producto_model.py (Productos)
Proporciona estadísticas y datos agregados para mostrar en el dashboard.
"""
from core.database import db
from models.cliente_model import Cliente
from models.servicio_model import Servicio
from models.pago_model import Pago
from models.producto_model import Producto

class Dashboard:
    """
    Métodos estáticos para obtener información agregada
    y mostrarla en el panel principal del sistema.
    """

    @staticmethod
    def total_clientes():
        """Retorna el total de clientes registrados."""
        return Cliente.query.count()

    @staticmethod
    def total_servicios_realizados():
        """Retorna el total de servicios realizados (proviene de ServicioRealizado)."""
        from models.servicios_realizado_model import ServicioRealizado
        return ServicioRealizado.query.count()

    @staticmethod
    def total_ingresos():
        """Calcula el total de ingresos sumando todos los pagos registrados."""
        pagos = Pago.query.all()
        return sum([p.monto for p in pagos])

    @staticmethod
    def productos_bajo_stock(min_stock=5):
        """Retorna la lista de productos cuyo stock es menor o igual a min_stock."""
        return Producto.query.filter(Producto.stock <= min_stock).all()
