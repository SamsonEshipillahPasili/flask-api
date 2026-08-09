from flask import Flask
from app.extensions import db, migrate
from app.errors import register_error_handlers


def create_app(config_object: str = 'app.config.ProductionConfig') -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    # init any app-extensions here.
    db.init_app(app)
    migrate.init_app(app, db)

    # register models
    from app import models

    # register error handlers
    register_error_handlers(app)

    # register app blueprints
    from app.routes import routes
    app.register_blueprint(routes, url_prefix='/api')
    return app

