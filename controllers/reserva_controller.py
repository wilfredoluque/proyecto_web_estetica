from flask import Blueprint, request, redirect, url_for,render_template
from models.reserva_model import Reserva
from models.cliente_model import Cliente
from models.servicio_model import Servicio
from models.usuario_model import Usuario
from views import reserva_view
from datetime import datetime

reserva_bp = Blueprint("reserva", __name__, url_prefix="/reservas")

@reserva_bp.route("/")
def index():
    reservas = Reserva.get_all()
    return reserva_view.list(reservas)


@reserva_bp.route("/create", methods=["GET","POST"])
def create():
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    empleados = Usuario.get_all()

    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        empleado_id = int(request.form["empleado_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        estado = request.form.get("estado", "Pendiente")
        nueva = Reserva(cliente_id, servicio_id, empleado_id, fecha, estado)
        nueva.save()
        return redirect(url_for("reserva.index"))
    return reserva_view.create(clientes, servicios,empleados)

@reserva_bp.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    reserva = Reserva.get_by_id(id)
    clientes = Cliente.get_all()
    servicios = Servicio.get_all()
    empleados = Usuario.get_all()
    if request.method == "POST":
        cliente_id = int(request.form["cliente_id"])
        servicio_id = int(request.form["servicio_id"])
        empleado_id = int(request.form["empleado_id"])
        fecha = datetime.strptime(request.form["fecha"], "%Y-%m-%d")
        estado = request.form.get("estado", reserva.estado)
        reserva.update(cliente_id, servicio_id, empleado_id, fecha, estado)
        return redirect(url_for("reserva.index"))
    return reserva_view.edit(reserva, clientes, servicios,empleados)

@reserva_bp.route("/delete/<int:id>")
def delete(id):
    reserva = Reserva.get_by_id(id)
    reserva.delete()
    return redirect(url_for("reserva.index"))


@reserva_bp.route("/calendar")
def calendar():
    reservas = Reserva.get_all()

    # Construir lista de eventos en Python (evitamos errores JS/Jinja)
    events = []
    for r in reservas:
        # aseguramos que url_for use el endpoint correcto 'reserva.edit'
        events.append({
            "title": f"{r.servicio.nombre} - {r.cliente.nombre}",
            "start": r.fecha.strftime("%Y-%m-%d"),
            "url": url_for("reserva.edit", id=r.id),
            "color": "orange" if r.estado == "Pendiente" else ("green" if r.estado == "Confirmada" else "red")
        })

    # Pasar reservas para la lista tradicional y events para el calendario
    return reserva_view.calendar(reservas, events)

