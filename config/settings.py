import os

class Config:
    SECRET_KEY = "SUPER-KEY-ESTETICA"  # cambiar en producción
    SQLALCHEMY_DATABASE_URI = "sqlite:///estetica.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
