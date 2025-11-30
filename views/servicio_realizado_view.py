from flask import render_template

def list(realizados):
    return render_template("servicios_realizados/index.html", realizados=realizados)

def create(clientes, servicios):
    return render_template("servicios_realizados/create.html", clientes=clientes, servicios=servicios)

def edit(realizado, clientes, servicios):
    return render_template("servicios_realizados/edit.html", realizado=realizado, clientes=clientes, servicios=servicios)
