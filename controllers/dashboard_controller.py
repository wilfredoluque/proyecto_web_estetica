from flask import Blueprint, render_template
from models.cliente_model import Cliente
from models.servicios_realizado_model import ServicioRealizado
from models.pago_model import Pago

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@dashboard_bp.route("/")
def index():
    total_clientes = len(Cliente.get_all())
    total_servicios_realizados = len(ServicioRealizado.get_all())
    total_ingresos = sum([s.precio for s in ServicioRealizado.get_all()])
    total_pagos = sum([p.monto for p in Pago.get_all()])

    return render_template(
        "dashboard/index.html",
        total_clientes=total_clientes,
        total_servicios_realizados=total_servicios_realizados,
        total_ingresos=total_ingresos,
        total_pagos=total_pagos
    )
