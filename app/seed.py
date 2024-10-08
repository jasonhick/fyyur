from datetime import datetime

from app import db
from app.models import Artist, Show, Venue


def seed_data():
    # Check if data already exists
    if Venue.query.first() or Artist.query.first() or Show.query.first():
        print("Data already exists. Skipping seed.")
        return

    # Create sample venues
    venue1 = Venue(
        name="O2 Academy Brixton",
        city="London",
        county="England",
        address="211 Stockwell Rd, London SW9 9SL",
        phone="+44 20 7771 3000",
        website="https://www.academymusicgroup.com/o2academybrixton/",
        facebook_link="https://www.facebook.com/O2AcademyBrixton/",
        seeking_talent=False,
        seeking_description="",
        image_link="https://static.ra.co/images/clubs/lg/o2brixton.jpg?dateUpdated=1531475782677",
    )

    venue2 = Venue(
        name="Rock City",
        city="Nottingham",
        county="Nottinghamshire",
        address="8 Talbot St, Nottingham NG1 5GG",
        phone="+44 115 950 6547",
        website="https://www.rock-city.co.uk/",
        facebook_link="https://www.facebook.com/rockcitynottingham/",
        seeking_talent=False,
        seeking_description="",
        image_link="https://www.rock-city.co.uk/wp-content/uploads/2020/02/2020-Rock-City-Exterior.jpg",
    )

    venue3 = Venue(
        name="Mountford Hall",
        city="Liverpool",
        county="Merseyside",
        address="160 Mount Pleasant, Liverpool L3 5TR",
        phone="+44 151 794 6868",
        website="https://www.liverpoolguild.org/",
        facebook_link="https://www.facebook.com/liverpoolguild",
        seeking_talent=False,
        seeking_description="",
        image_link="https://ichef.bbci.co.uk/images/ic/1920x1080/p071fc7v.jpg",
    )

    venue4 = Venue(
        name="Clwb Ifor Bach",
        city="Cardiff",
        county="Wales",
        address="11 Womanby St, Cardiff CF10 1BR",
        phone="+44 29 2023 2199",
        website="https://www.clwb.net/",
        facebook_link="https://www.facebook.com/clwbiforbach",
        seeking_talent=True,
        seeking_description="Looking for emerging Welsh talent.",
        image_link="https://clwb.net/wp-content/uploads/2023/07/web-image-3.jpg",
    )

    venue5 = Venue(
        name="Heaven",
        city="London",
        county="England",
        address="Under the Arches, Villiers St, Charing Cross, London WC2N 6NG",
        phone="+44 20 7930 2020",
        website="https://heaven-live.co.uk/",
        facebook_link="https://www.facebook.com/HeavenNightclub/",
        seeking_talent=False,
        seeking_description="",
        image_link="https://thatsup.co.uk/content/img/place/h/e/heaven-2.jpg",
    )

    # Create sample artists
    # artist1 = Artist(
    #     name="Guns N Petals", city="San Francisco", county="CA", phone="326-123-5000"
    # )
    # artist2 = Artist(
    #     name="Matt Quevedo", city="New York", county="NY", phone="300-400-5000"
    # )

    # # Create sample shows
    # show1 = Show(artist_id=1, venue_id=1, start_time=datetime(2023, 5, 21, 21, 30))
    # show2 = Show(artist_id=2, venue_id=2, start_time=datetime(2023, 6, 15, 20, 00))

    # Add to session and commit
    db.session.add_all([venue1, venue2, venue3, venue4, venue5])
    db.session.commit()

    print("Seed data added successfully!")
