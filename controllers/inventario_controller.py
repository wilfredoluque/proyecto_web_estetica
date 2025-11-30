from flask import Blueprint, request, redirect, url_for
from models.inventario_model import Inventario
from models.producto_model import Producto
from views import inventario_view
from config.security import requiere_admin

inventario_bp = Blueprint("inventario", __name__, url_prefix="/inventario")

@inventario_bp.route("/")
def index():
    inventarios = Inventario.get_all()
    return inventario_view.list(inventarios)

@inventario_bp.route("/create", methods=["GET","POST"])
@requiere_admin
def create():
    productos = Producto.get_all()
    if request.method == "POST":
        producto_id = int(request.form["producto_id"])
        cantidad = int(request.form["cantidad"])
        ubicacion = request.form.get("ubicacion", "")
        nuevo = Inventario(producto_id, cantidad, ubicacion)
        nuevo.save()
        return redirect(url_for("inventario.index"))
    return inventario_view.create(productos)

@inventario_bp.route("/edit/<int:id>", methods=["GET","POST"])
@requiere_admin
def edit(id):
    inventario = Inventario.get_by_id(id)
    productos = Producto.get_all()
    if request.method == "POST":
        producto_id = int(request.form["producto_id"])
        cantidad = int(request.form["cantidad"])
        ubicacion = request.form.get("ubicacion", "")
        inventario.update(producto_id, cantidad, ubicacion)
        return redirect(url_for("inventario.index"))
    return inventario_view.edit(inventario, productos)

@inventario_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    inventario = Inventario.get_by_id(id)
    inventario.delete()
    return redirect(url_for("inventario.index"))
