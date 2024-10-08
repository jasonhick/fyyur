from app import db


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # genres = db.Column(db.ARRAY(db.String), nullable=True)
    city = db.Column(db.String(120), nullable=True)
    state = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    # shows = db.relationship("Show", backref="artist", cascade="all, delete")

    # upcoming_shows_count = db.Column(db.Integer, default=0)
    # upcoming_shows = db.Column(db.PickleType)
    # past_shows_count = db.Column(db.Integer, default=0)
    # past_shows = db.Column(db.PickleType)
