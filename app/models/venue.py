from app import db


class Venue(db.Model):

    __tablename__ = "venues"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    county = db.Column(db.String(120), nullable=True)
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String()), nullable=True)
    image_link = db.Column(db.String(500))
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    seeking_description = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=False)
    website = db.Column(db.String(500))
    shows = db.relationship("Show", backref="venue", cascade="all, delete")

    def __repr__(self):
        return f"<Venue {self.id} {self.name}>"
