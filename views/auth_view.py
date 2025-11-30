from flask import render_template

def login(error=None):
    return render_template("login/login.html", error=error)

def register():
    return render_template("login/register.html")
