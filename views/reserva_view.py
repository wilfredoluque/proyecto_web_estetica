from flask import render_template

def list(reservas):
    return render_template("reservas/index.html", reservas=reservas)

def create(clientes, servicios, empleados):
    return render_template("reservas/create.html", clientes=clientes, servicios=servicios, empleados=empleados)

def edit(reserva, clientes, servicios, empleados):
    return render_template("reservas/edit.html", reserva=reserva, clientes=clientes, servicios=servicios, empleados=empleados)


def calendar(reservas, events):
    # events es una lista de dicts (no JSON string) — la plantilla usará tojson
    return render_template("reservas/calendar.html", reservas=reservas, events=events)