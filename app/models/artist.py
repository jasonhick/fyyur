from app import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(120), nullable=True)
    county = db.Column(db.String(120), nullable=True)
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), nullable=True)
    image_link = db.Column(db.String(500))
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    seeking_description = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False)
    website = db.Column(db.String(500))
    # shows = db.relationship("Show", backref="artist", cascade="all, delete")

    # upcoming_shows_count = db.Column(db.Integer, default=0)
    # upcoming_shows = db.Column(db.PickleType)
    # past_shows_count = db.Column(db.Integer, default=0)
    # past_shows = db.Column(db.PickleType)
