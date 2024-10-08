import logging

from flask_migrate import Migrate

from app import create_app, db
from app.models import Artist, Show, Venue
from app.seed import seed_data

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the Flask app
app = create_app()

# Set up database migration
migrate = Migrate(app, db)

# Run the application
if __name__ == "__main__":
    with app.app_context():
        # Seed the database
        logger.debug("Attempting to seed database tables...")
        try:
            seed_data()
        except Exception as e:
            logger.error(f"Error seeding database tables: {str(e)}")

    # Run the app in debug mode
    app.run(debug=True)
