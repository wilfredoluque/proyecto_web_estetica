from flask import render_template

def list(registros):
    return render_template("historial/index.html", registros=registros)

def create(clientes, servicios, empleados):
    return render_template("historial/create.html", clientes=clientes, servicios=servicios, empleados=empleados)

def edit(registro, clientes, servicios, empleados):
    return render_template("historial/edit.html", registro=registro, clientes=clientes, servicios=servicios, empleados=empleados)
