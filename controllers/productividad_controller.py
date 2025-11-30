from flask import Blueprint, request, redirect, url_for
from models.productividad_model import Productividad
from models.usuario_model import Usuario
from views import productividad_view
from config.security import requiere_admin
from datetime import datetime

productividad_bp = Blueprint("productividad", __name__, url_prefix="/productividad")

@productividad_bp.route("/")
def index():
    registros = Productividad.get_all()
    return productividad_view.list(registros)

@productividad_bp.route("/create", methods=["GET", "POST"])
def create():
    empleados = Usuario.get_all()
    if request.method == "POST":
        empleado_id = int(request.form["empleado_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        clientes = int(request.form.get("clientes_atendidos", 0))
        ventas = float(request.form.get("ventas_realizadas", 0))
        horas = float(request.form.get("horas_trabajadas", 0))
        obs = request.form.get("observacion", "")
        
        reg = Productividad(empleado_id, fecha, clientes, ventas, horas, obs)
        reg.save()
        return redirect(url_for("productividad.index"))
    
    return productividad_view.create(empleados)

@productividad_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@requiere_admin
def edit(id):
    reg = Productividad.get_by_id(id)
    empleados = Usuario.get_all()
    
    if request.method == "POST":
        empleado_id = int(request.form["empleado_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        clientes = int(request.form.get("clientes_atendidos", 0))
        ventas = float(request.form.get("ventas_realizadas", 0))
        horas = float(request.form.get("horas_trabajadas", 0))
        obs = request.form.get("observacion", "")
        
        reg.update(empleado_id, fecha, clientes, ventas, horas, obs)
        return redirect(url_for("productividad.index"))
    
    return productividad_view.edit(reg, empleados)

@productividad_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    reg = Productividad.get_by_id(id)
    reg.delete()
    return redirect(url_for("productividad.index"))
