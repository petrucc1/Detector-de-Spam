from flask import Flask # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from .config import Config

# Inicializando a extensão SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializando a extensão com a aplicação Flask
    db.init_app(app)

    with app.app_context():
        # Importando rotas e modelos após criar o contexto da aplicação
        from . import routes, models
        db.create_all()  # Criando tabelas no banco de dados
        app.register_blueprint(routes.main)

    return app
