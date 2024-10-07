from datetime import datetime

from app import create_app, db
from app.models import Artist, Show, Venue


def seed_data():
    # Check if data already exists
    if Venue.query.first() or Artist.query.first() or Show.query.first():
        print("Data already exists. Skipping seed.")
        return

    # Create sample venues
    venue1 = Venue(
        name="The Musical Hop",
        city="San Francisco",
        state="CA",
        address="1015 Folsom Street",
        phone="123-123-1234",
    )
    venue2 = Venue(
        name="The Dueling Pianos Bar",
        city="New York",
        state="NY",
        address="335 Delancey Street",
        phone="914-003-1132",
    )

    # Create sample artists
    artist1 = Artist(
        name="Guns N Petals", city="San Francisco", state="CA", phone="326-123-5000"
    )
    artist2 = Artist(
        name="Matt Quevedo", city="New York", state="NY", phone="300-400-5000"
    )

    # Create sample shows
    show1 = Show(artist_id=1, venue_id=1, start_time=datetime(2023, 5, 21, 21, 30))
    show2 = Show(artist_id=2, venue_id=2, start_time=datetime(2023, 6, 15, 20, 00))

    # Add to session and commit
    db.session.add_all([venue1, venue2, artist1, artist2, show1, show2])
    db.session.commit()

    print("Seed data added successfully!")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()
