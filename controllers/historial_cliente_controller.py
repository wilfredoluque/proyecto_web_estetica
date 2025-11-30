from flask import Blueprint, request, redirect, url_for
from models.historial_cliente_model import HistorialServicio
from models.cliente_model import Cliente
from models.servicio_model import Servicio
from models.usuario_model import Usuario
from views import historial_cliente_view
from config.security import requiere_admin
from datetime import datetime

historial_bp = Blueprint("historial", __name__, url_prefix="/historial")

@historial_bp.route("/")
def index():
    registros = HistorialServicio.get_all()
    return historial_cliente_view.list(registros)

# Crear (empleado y admin pueden crear)
@historial_bp.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    empleados = Usuario.get_all()
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        empleado_id = int(request.form.get("empleado_id") or 0) or None
        fecha_str = request.form.get("fecha")
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d") if fecha_str else datetime.now()
        estado = request.form.get("estado", "Realizado")
        satisfaccion = request.form.get("satisfaccion", "Bueno")
        comentario = request.form.get("comentario", "")
        registro = HistorialServicio(cliente_id, servicio_id, empleado_id, fecha, estado, satisfaccion, comentario)
        registro.save()
        return redirect(url_for("historial.index"))
    return historial_cliente_view.create(clientes, servicios, empleados)

# Editar (solo admin)
@historial_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@requiere_admin
def edit(id):
    registro = HistorialServicio.get_by_id(id)
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    empleados = Usuario.get_all()
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        empleado_id = int(request.form.get("empleado_id") or 0) or None
        fecha_str = request.form.get("fecha")
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d") if fecha_str else registro.fecha
        estado = request.form.get("estado", registro.estado)
        satisfaccion = request.form.get("satisfaccion", registro.satisfaccion)
        comentario = request.form.get("comentario", registro.comentario)
        registro.update(cliente_id=cliente_id, servicio_id=servicio_id, empleado_id=empleado_id, fecha=fecha, estado=estado, satisfaccion=satisfaccion, comentario=comentario)
        return redirect(url_for("historial.index"))
    return historial_cliente_view.edit(registro, clientes, servicios, empleados)

# Delete (solo admin)
@historial_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    reg = HistorialServicio.get_by_id(id)
    reg.delete()
    return redirect(url_for("historial.index"))
