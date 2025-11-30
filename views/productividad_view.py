from flask import render_template

def list(registros):
    return render_template("productividad/index.html", registros=registros)

def create(empleados):
    return render_template("productividad/create.html", empleados=empleados)

def edit(registro, empleados):
    return render_template("productividad/edit.html", registro=registro, empleados=empleados)
