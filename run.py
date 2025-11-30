"""
run.py — Archivo principal del sistema
Proyecto Estética — Wilfredo
"""

import os
from flask import Flask, request, render_template
from config.settings import Config
from core.database import db
from datetime import datetime

# ---------------------------------------------------------
# BLUEPRINTS
# ---------------------------------------------------------
from controllers.auth_controller import auth_bp
from controllers.usuario_controller import usuario_bp
from controllers.cliente_controller import cliente_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.servicio_controller import servicio_bp
from controllers.servicio_realizado_controller import servicio_realizado_bp
from controllers.pago_controller import pago_bp
from controllers.producto_controller import producto_bp
from controllers.reserva_controller import reserva_bp
from controllers.inventario_controller import inventario_bp
from controllers.productividad_controller import productividad_bp
from controllers.historial_cliente_controller import historial_bp


# ---------------------------------------------------------
# CREAR APP
# ---------------------------------------------------------
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ---------------------------
    # BASE DE DATOS
    # ---------------------------
    db.init_app(app)

    # ---------------------------
    # REGISTRO DE BLUEPRINTS
    # ---------------------------
    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(servicio_bp)
    app.register_blueprint(servicio_realizado_bp)
    app.register_blueprint(pago_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(reserva_bp)
    app.register_blueprint(inventario_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(productividad_bp)
    app.register_blueprint(historial_bp)

    # ---------------------------
    # GOOGLE AUTH CONFIG — FINAL (comentado)
    # ---------------------------
    """
    @app.before_request
    def load_google_flow():
        from google_auth_oauthlib.flow import Flow
        GOOGLE_CLIENT_SECRETS = "/etc/secrets/google_client.json"

        if not os.path.exists(GOOGLE_CLIENT_SECRETS):
            print("⚠ ERROR: google_client.json NO existe en Render")
            return

        if app.config["ENV"] == "development":
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        REDIRECT_URI = os.getenv(
            "GOOGLE_REDIRECT_URI",
            "http://localhost:5000/auth/google/callback"
        )

        app.google_flow = Flow.from_client_secrets_file(
            GOOGLE_CLIENT_SECRETS,
            scopes=[
                "openid",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
            ],
            redirect_uri=REDIRECT_URI
        )
    """

    # ---------------------------
    # NAVBAR ACTIVO
    # ---------------------------
    @app.context_processor
    def utility_processor():
        def is_active(path):
            return "active" if request.path.rstrip("/") == path.rstrip("/") else ""
        return dict(is_active=is_active)

    # ---------------------------
    # LANDING PAGE
    # ---------------------------
    @app.route("/")
    def home():
        return render_template("landing/index.html")

    # ---------------------------
    # AÑO GLOBAL
    # ---------------------------
    @app.context_processor
    def inject_year():
        return {"current_year": datetime.now().year}

    return app


# ---------------------------------------------------------
# EXPOSE APP PARA GUNICORN
# ---------------------------------------------------------
app = create_app()
with app.app_context():
    db.create_all()


# ---------------------------------------------------------
# EJECUCIÓN LOCAL
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
