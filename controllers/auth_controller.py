from flask import Blueprint, request, redirect, url_for, session
from models.usuario_model import Usuario
from views import auth_view

# GOOGLE LOGIN IMPORTS
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
import google.auth.transport.requests
from pip._vendor import cachecontrol
import requests
import pathlib
import os

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")
"""
# Permitir HTTP en local
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Ruta del archivo google_client.json
if os.environ.get("RENDER") == "1":
    # En Render
    GOOGLE_CLIENT_SECRETS_FILE = "/etc/secrets/google_client.json"
else:
    # Local
    GOOGLE_CLIENT_SECRETS_FILE = os.path.join(
        pathlib.Path(__file__).parent.parent,
        "core",
        "google_client.json"
    )

# Configurar Google OAuth
flow = Flow.from_client_secrets_file(
    GOOGLE_CLIENT_SECRETS_FILE,
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid"
    ],
    redirect_uri="http://localhost:5000/auth/google/callback"
)
"""
# ============================================
# 🔵 LOGIN CON GOOGLE
# ============================================

@auth_bp.route("/login/google")
def login_google():
    auth_url, _ = flow.authorization_url()
    return redirect(auth_url)


@auth_bp.route("/google/callback")
def google_callback():
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    token_request = google.auth.transport.requests.Request()
    id_info = id_token.verify_oauth2_token(
        credentials.id_token,
        token_request,
        audience=flow.client_config["client_id"]
    )

    # Guardar datos en sesión
    session["usuario_id"] = id_info["email"]
    session["usuario_nombre"] = id_info["name"]
    session["usuario_rol"] = "cliente"   # por defecto

    return redirect(url_for("dashboard.index"))

# ============================================
# 🔵 LOGIN NORMAL (USUARIOS DEL SISTEMA)
# ============================================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        usuario = Usuario.get_by_email(email)

        if usuario and usuario.check_password(password):
            session["usuario_id"] = usuario.id
            session["usuario_nombre"] = usuario.nombre
            session["usuario_rol"] = usuario.rol
            return redirect(url_for("dashboard.index"))

        return auth_view.login(error="Credenciales incorrectas")

    return auth_view.login()

# ============================================
# 🔵 REGISTRO NORMAL
# ============================================

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        password = request.form["password"]

        nuevo = Usuario(nombre, email, password)
        nuevo.save()

        return redirect(url_for("auth.login"))

    return auth_view.register()

# ============================================
# 🔵 LOGOUT
# ============================================

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
