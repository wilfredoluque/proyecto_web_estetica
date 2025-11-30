from flask import render_template

def list(servicios):
    return render_template("servicios/index.html", servicios=servicios)

def create():
    return render_template("servicios/create.html")

def edit(servicio):
    return render_template("servicios/edit.html", servicio=servicio)
