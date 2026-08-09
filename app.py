from flask import Flask
from extensions import db, migrate
from errors import register_error_handlers


def create_app(config_object: str = 'config.ProductionConfig') -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    # init any app-extensions here.
    db.init_app(app)
    migrate.init_app(app, db)

    # register models
    import models

    # register error handlers
    register_error_handlers(app)

    # register app blueprints
    from routes import routes
    app.register_blueprint(routes, url_prefix='/api')
    return app

