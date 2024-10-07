from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Venue(db.Model):

    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    # shows = db.relationship("Show", backref="venue", lazy=True)

    # upcoming_shows_count = db.Column(db.Integer, default=0)
    # upcoming_shows = db.Column(db.PickleType)
    # past_shows_count = db.Column(db.Integer, default=0)
    # past_shows = db.Column(db.PickleType)

    def __repr__(self):
        return f"<Venue {self.id} {self.name}>"
