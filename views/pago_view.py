from flask import render_template

def list(pagos):
    return render_template("pagos/index.html", pagos=pagos)

def create(clientes):
    return render_template("pagos/create.html", clientes=clientes)

def create(servicios_realizados):
    return render_template("pagos/create.html", servicios_realizados=servicios_realizados)

