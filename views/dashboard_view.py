from flask import render_template

def index(stats, chart):
    return render_template("dashboard/index.html", stats=stats, chart=chart)
