from flask import Blueprint, request, redirect, url_for
from models.producto_model import Producto
from views import producto_view
from config.security import requiere_admin

producto_bp = Blueprint("producto", __name__, url_prefix="/productos")

@producto_bp.route("/")
def index():
    productos = Producto.get_all()
    return producto_view.list(productos)

@producto_bp.route("/create", methods=["GET","POST"])
@requiere_admin
def create():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form.get("descripcion", "")
        precio = float(request.form["precio"])
        stock = int(request.form["stock"])
        nuevo = Producto(nombre, descripcion, precio, stock)
        nuevo.save()
        return redirect(url_for("producto.index"))
    return producto_view.create()

@producto_bp.route("/edit/<int:id>", methods=["GET","POST"])
@requiere_admin
def edit(id):
    producto = Producto.get_by_id(id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form.get("descripcion", "")
        precio = float(request.form["precio"])
        stock = int(request.form["stock"])
        producto.update(nombre, descripcion, precio, stock)
        return redirect(url_for("producto.index"))
    return producto_view.edit(producto)

@producto_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    producto = Producto.get_by_id(id)
    producto.delete()
    return redirect(url_for("producto.index"))
