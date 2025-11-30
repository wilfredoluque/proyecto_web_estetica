from flask import render_template

def list(inventarios):
    return render_template("inventario/index.html", inventarios=inventarios)

def create(productos):
    return render_template("inventario/create.html", productos=productos)

def edit(inventario, productos):
    return render_template("inventario/edit.html", inventario=inventario, productos=productos)
