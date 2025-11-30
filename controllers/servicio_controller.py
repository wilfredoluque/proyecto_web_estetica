from flask import Blueprint, request, redirect, url_for
from models.servicio_model import Servicio
from views import servicio_view
from config.security import requiere_admin

servicio_bp = Blueprint("servicio", __name__, url_prefix="/servicios")

@servicio_bp.route("/")
def index():
    servicios = Servicio.get_all()
    return servicio_view.list(servicios)

@servicio_bp.route("/create", methods=["GET","POST"])
@requiere_admin
def create():
    if request.method=="POST":
        nombre = request.form["nombre"]
        descripcion = request.form.get("descripcion")
        precio = float(request.form["precio"])
        nuevo = Servicio(nombre, descripcion, precio)
        nuevo.save()
        return redirect(url_for("servicio.index"))
    return servicio_view.create()

@servicio_bp.route("/edit/<int:id>", methods=["GET","POST"])
@requiere_admin
def edit(id):
    servicio = Servicio.get_by_id(id)
    if request.method=="POST":
        nombre = request.form["nombre"]
        descripcion = request.form.get("descripcion")
        precio = float(request.form["precio"])
        servicio.update(nombre, descripcion, precio)
        return redirect(url_for("servicio.index"))
    return servicio_view.edit(servicio)

@servicio_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    servicio = Servicio.get_by_id(id)
    servicio.delete()
    return redirect(url_for("servicio.index"))
