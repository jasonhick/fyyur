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
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_venue = db.Column(db.Boolean, default=False)
    website_link = db.Column(db.String(500))
    shows = db.relationship("Show", backref="artist", cascade="all, delete")

    # used to debug data
    def to_dict(self):
        """Convert the SQLAlchemy model instance to a dictionary."""
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
