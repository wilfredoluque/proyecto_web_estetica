from flask import Blueprint, request, redirect, url_for
from models.servicios_realizado_model import ServicioRealizado
from models.cliente_model import Cliente
from models.servicio_model import Servicio
from views import servicio_realizado_view
from datetime import datetime
from config.security import requiere_admin

servicio_realizado_bp = Blueprint("servicio_realizado", __name__, url_prefix="/servicios_realizados")

@servicio_realizado_bp.route("/")
def index():
    realizados = ServicioRealizado.get_all()
    return servicio_realizado_view.list(realizados)

@servicio_realizado_bp.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        precio = float(request.form["precio"])
        
        nuevo = ServicioRealizado(cliente_id, servicio_id, fecha, precio)
        nuevo.save()
        return redirect(url_for("servicio_realizado.index"))
    
    return servicio_realizado_view.create(clientes, servicios)

@servicio_realizado_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    realizado = ServicioRealizado.get_by_id(id)
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        precio = float(request.form["precio"])
        
        realizado.update(cliente_id, servicio_id, fecha, precio)
        return redirect(url_for("servicio_realizado.index"))
    
    return servicio_realizado_view.edit(realizado, clientes, servicios)

@servicio_realizado_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    realizado = ServicioRealizado.get_by_id(id)
    realizado.delete()
    return redirect(url_for("servicio_realizado.index"))
