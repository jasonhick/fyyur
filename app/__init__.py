# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import collections
import collections.abc
import logging
from logging import FileHandler, Formatter

import babel
import dateutil.parser
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.routes import artists_bp, shows_bp, venues_bp
from forms import *

from .config import Config

collections.Callable = collections.abc.Callable

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Create and configure the Flask application.

    This function sets up the Flask app, initializes extensions, registers routes and blueprints,
    configures Jinja filters, and sets up logging for non-debug environments.

    Returns:
        Flask: The configured Flask application instance.
    """
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # ----------------------------------------------------------------------------#
    # Routes
    # ----------------------------------------------------------------------------#

    # Home and Error Handlers
    @app.route("/")
    def index():
        return render_template("pages/home.html")

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("errors/500.html"), 500

    # Register blueprints
    app.register_blueprint(artists_bp, url_prefix="/artists")
    app.register_blueprint(shows_bp, url_prefix="/shows")
    app.register_blueprint(venues_bp, url_prefix="/venues")

    # Add custom Jinja filter for datetime formatting
    app.jinja_env.filters["datetime"] = format_datetime

    # Activate logging for non-debug environments
    if not app.debug:
        file_handler = FileHandler("error.log")
        file_handler.setFormatter(
            Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info("errors")

    return app


# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#
def format_datetime(value, format="medium"):
    date = dateutil.parser.parse(value)
    if format == "full":
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == "medium":
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale="en")
