from datetime import datetime

from flask_wtf import FlaskForm as Form
from wtforms import (
    BooleanField,
    DateTimeField,
    SelectField,
    SelectMultipleField,
    StringField,
)
from wtforms.validators import URL, DataRequired

from app.models import Artist, Venue

# Define the list of counties as a constant
COUNTIES = [
    "Bedfordshire",
    "Berkshire",
    "Bristol",
    "Buckinghamshire",
    "Cambridgeshire",
    "Cheshire",
    "City of London",
    "Cornwall",
    "Cumbria",
    "Derbyshire",
    "Devon",
    "Dorset",
    "Durham",
    "East Riding of Yorkshire",
    "East Sussex",
    "Essex",
    "Gloucestershire",
    "Greater London",
    "Greater Manchester",
    "Hampshire",
    "Herefordshire",
    "Hertfordshire",
    "Isle of Wight",
    "Kent",
    "Lancashire",
    "Leicestershire",
    "Lincolnshire",
    "Merseyside",
    "Norfolk",
    "North Yorkshire",
    "Northamptonshire",
    "Northumberland",
    "Nottinghamshire",
    "Oxfordshire",
    "Rutland",
    "Shropshire",
    "Somerset",
    "South Yorkshire",
    "Staffordshire",
    "Suffolk",
    "Surrey",
    "Tyne and Wear",
    "Warwickshire",
    "West Midlands",
    "West Sussex",
    "West Yorkshire",
    "Wiltshire",
    "Worcestershire",
]

# Define the list of genres as a constant
GENRES = [
    "Alternative",
    "Blues",
    "Classical",
    "Country",
    "Electronic",
    "Folk",
    "Funk",
    "Hip-Hop",
    "Heavy Metal",
    "Instrumental",
    "Jazz",
    "Musical Theatre",
    "Pop",
    "Punk",
    "R&B",
    "Reggae",
    "Rock n Roll",
    "Soul",
    "Other",
]


def get_artists():
    return Artist.query.all()


def get_venues():
    return Venue.query.all()


class ShowForm(Form):
    artist_id = SelectField(
        "artist_id", choices=[], validators=[DataRequired()]
    )
    venue_id = SelectField("venue_id", choices=[], validators=[DataRequired()])
    start_time = DateTimeField(
        "start_time", validators=[DataRequired()], default=datetime.today()
    )

    def __init__(self, *args, **kwargs):
        super(ShowForm, self).__init__(*args, **kwargs)
        # Add a default option at the start of the choices
        self.artist_id.choices = [("", "Select an artist")] + [
            (artist.id, artist.name) for artist in get_artists()
        ]
        self.venue_id.choices = [("", "Select a venue")] + [
            (venue.id, venue.name) for venue in get_venues()
        ]


class VenueForm(Form):
    name = StringField("name", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    county = SelectField(
        "county",
        validators=[DataRequired()],
        choices=[(county, county) for county in COUNTIES],
    )
    address = StringField("address", validators=[DataRequired()])
    phone = StringField("phone")
    image_link = StringField("image_link")
    genres = SelectMultipleField(
        "genres",
        validators=[DataRequired()],
        choices=[(genre, genre) for genre in GENRES],
    )
    facebook_link = StringField("facebook_link", validators=[URL()])
    website_link = StringField("website_link")
    seeking_talent = BooleanField("seeking_talent")
    seeking_description = StringField("seeking_description")


class ArtistForm(Form):
    name = StringField("name", validators=[DataRequired()])
    city = StringField("city", validators=[DataRequired()])
    county = SelectField(
        "county",
        validators=[DataRequired()],
        choices=[(county, county) for county in COUNTIES],
    )
    phone = StringField(
        "phone",
        validators=[DataRequired()],
    )
    image_link = StringField("image_link")
    genres = SelectMultipleField(
        "genres",
        validators=[DataRequired()],
        choices=[(genre, genre) for genre in GENRES],
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        "facebook_link",
        validators=[URL()],
    )

    website_link = StringField("website_link")
    seeking_venue = BooleanField("seeking_venue")
    seeking_description = StringField("seeking_description")
