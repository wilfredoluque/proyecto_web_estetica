from core.database import db
from flask import Blueprint, request, redirect, url_for
from models.usuario_model import Usuario
from views import usuario_view
from config.security import requiere_admin

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")


@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)


@usuario_bp.route("/create", methods=["GET", "POST"])
@requiere_admin
def create():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]
        rol = request.form.get("rol", "empleado")

        nuevo = Usuario(nombre, email, password, rol)
        nuevo.save()
        return redirect(url_for("usuario.index"))

    return usuario_view.create()


@usuario_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@requiere_admin
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        rol = request.form.get("rol", usuario.rol)
        password = request.form.get("password", None)

        usuario.update(nombre=nombre, email=email, rol=rol, password=password)
        return redirect(url_for("usuario.index"))

    return usuario_view.edit(usuario)


@usuario_bp.route("/delete/<int:id>")
@requiere_admin
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for("usuario.index"))
