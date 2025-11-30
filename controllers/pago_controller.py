from flask import Blueprint, request, redirect, url_for
from models.pago_model import Pago
from models.cliente_model import Cliente
from views import pago_view
from datetime import datetime
from config.security import requiere_admin
from models.servicios_realizado_model import ServicioRealizado



pago_bp = Blueprint("pago", __name__, url_prefix="/pagos")

@pago_bp.route("/")
def index():
    pagos = Pago.get_all()
    return pago_view.list(pagos)

@pago_bp.route("/create", methods=["GET","POST"])
def create():
    servicios_realizados = ServicioRealizado.get_all()
    if request.method == "POST":
        servicio_realizado_id = int(request.form["servicio_realizado_id"])
        descripcion = request.form.get("descripcion", "")
        # OBTENER PRECIO DESDE SERVICIO REALIZADO
        servicio_realizado = ServicioRealizado.get_by_id(servicio_realizado_id)
        monto = round(servicio_realizado.precio, 2) if servicio_realizado else 0
        nuevo = Pago(
            cliente_id=servicio_realizado.cliente_id,
            fecha=datetime.now(),
            monto=monto,
            descripcion=descripcion
        )
        nuevo.save()
        return redirect(url_for("pago.index"))
    return pago_view.create(servicios_realizados)


@pago_bp.route("/edit/<int:id>", methods=["GET","POST"])
@requiere_admin
def edit(id):
    pago = Pago.get_by_id(id)
    clientes = Cliente.get_all()
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        monto = float(request.form["monto"])
        descripcion = request.form.get("descripcion", "")
        pago.update(cliente_id, fecha, monto, descripcion)
        return redirect(url_for("pago.index"))
    return pago_view.edit(pago, clientes)

@pago_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    pago = Pago.get_by_id(id)
    pago.delete()
    return redirect(url_for("pago.index"))
