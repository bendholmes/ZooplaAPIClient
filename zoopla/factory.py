from flask import Flask

def create_app(config='zoopla.config'):
    app = Flask(__name__)
    app.config.from_object(config)

    from .zoopla import DB
    DB.init_app(app)

    return app
