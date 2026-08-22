from flask import Flask

from .config import Config


def create_app() -> Flask:
    """"Creates the app used in the dashboard.

    Returns the application generated from the templates and the config.
    """
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)
    
    from .static import views
    app.register_blueprint(views.bp)

    return app 