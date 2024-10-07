from flask_migrate import Migrate

from app import create_app, db

# Create the Flask app
app = create_app()

# Set up database migration
migrate = Migrate(app, db)


# Run the application
if __name__ == "__main__":
    # Run the app in debug mode
    app.run(debug=True)
