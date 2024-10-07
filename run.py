import logging

from flask_migrate import Migrate

from app import create_app, db
from app.models import Artist, Show, Venue

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the Flask app
app = create_app(seed=False)

# Set up database migration
migrate = Migrate(app, db)

# Run the application
if __name__ == "__main__":
    with app.app_context():
        logger.debug("Attempting to create database tables...")
        try:
            db.create_all()
            logger.debug("Database tables created successfully.")
        except Exception as e:
            logger.error(f"Error creating database tables: {str(e)}")

    # Run the app in debug mode
    app.run(debug=True)
