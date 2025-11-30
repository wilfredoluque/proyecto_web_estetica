"""
run.py
-----------------------------------------
Archivo principal del proyecto Flask.
Aquí se inicializa la aplicación, la base
de datos, los blueprints y la configuración
general del sistema.
Autor: Wilfredo
Proyecto: Sistema de Gestión — Defensa Final
-----------------------------------------
"""
from flask import Flask, request, render_template
from config.settings import Config
from core.database import db
from google_auth_oauthlib.flow import Flow
import os
from datetime import datetime
# Instancia base de Flask
app = Flask(__name__)
app.secret_key = "clave_super_secreta"  # Clave necesaria para sesiones y cookies

# ---------------------------------------------------------
# CONFIGURACIÓN GOOGLE AUTH (Modo desarrollo)
# ---------------------------------------------------------
# Permite usar HTTP en lugar de HTTPS para pruebas locales
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
GOOGLE_CLIENT_SECRETS = "/etc/secrets/core/google_client.json"

# Flujo de autenticación con Google
# Aquí se cargan los datos del cliente y los permisos
flow = Flow.from_client_secrets_file(
    GOOGLE_CLIENT_SECRETS,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid"
    ],
    redirect_uri="http://localhost:5000/auth/google/callback"
)

# ---------------------------------------------------------
# IMPORTACIÓN DE BLUEPRINTS
# Cada módulo controla una parte del proyecto (separación lógica)
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



def create_app():#Función fábrica de Flask.Aquí se configura la app completa:Configuración generalBase de datosRegistro de blueprintsFunciones globales para templates
    app = Flask(__name__)
    app.config.from_object(Config)

    # --------------------------------------------
    # Inicializar conexión con la base de datos
    # --------------------------------------------
    db.init_app(app)

    # --------------------------------------------
    # Registrar todos los Blueprints del sistema
    # --------------------------------------------
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

    # ---------------------------------------------------------
    # NAVBAR ACTIVO
    # Función global que determina qué enlace está activo
    # ---------------------------------------------------------
    @app.context_processor
    def utility_processor():
        def is_active(path):
            return "active" if request.path.rstrip("/") == path.rstrip("/") else ""
        return dict(is_active=is_active)


    # ---------------------------------------------------------
    # RUTA PRINCIPAL DEL PROYECTO (Landing Page)
    # ---------------------------------------------------------
    @app.route("/")
    def home():
        # Renderiza la página inicial ubicada en templates/landing/index.html
        return render_template("landing/index.html")

    # ---------------------------------------------------------
    # INYECCIÓN GLOBAL DE FECHA
    # Permite mostrar el año actual en cualquier template
    # ---------------------------------------------------------
    @app.context_processor
    def inject_year():
        return {'current_year': datetime.now().year}
    return app

# ---------------------------------------------------------
# EJECUCIÓN PRINCIPAL DEL SERVIDOR
# ---------------------------------------------------------
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
