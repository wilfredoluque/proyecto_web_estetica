from flask import Blueprint, request, redirect, url_for
from core.database import db
from models.cliente_model import Cliente
from views import cliente_view
from config.security import requiere_admin

cliente_bp = Blueprint("cliente", __name__, url_prefix="/clientes")

@cliente_bp.route("/")
def index():
    clientes = Cliente.get_all()
    return cliente_view.list(clientes)

@cliente_bp.route("/create", methods=["GET", "POST"])

def create():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")

        nuevo = Cliente(nombre, email, telefono, direccion)
        nuevo.save()
        return redirect(url_for("cliente.index"))

    return cliente_view.create()

@cliente_bp.route("/edit/<int:id>", methods=["GET", "POST"])

def edit(id):
    cliente = Cliente.get_by_id(id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form.get("email")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")
        cliente.update(nombre, email, telefono, direccion)
        return redirect(url_for("cliente.index"))

    return cliente_view.edit(cliente)

@cliente_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    cliente = Cliente.get_by_id(id)
    cliente.delete()
    return redirect(url_for("cliente.index"))
