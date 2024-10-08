import os


class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/fyyur"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
