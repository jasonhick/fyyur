from datetime import datetime

from app import db
from app.models import Artist, Show, Venue


def seed_data():
    # Check if data already exists
    if Venue.query.first():
        print("Venue data already exists. Skipping...")
    else:
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

        db.session.add_all([venue1, venue2, venue3, venue4, venue5])
        db.session.commit()

    if Artist.query.first():
        print("Artist data already exists. Skipping...")
        return
    else:
        # Create sample artists
        artist1 = Artist(
            name="The Beatles",
            genres=["Rock", "Pop"],
            city="Liverpool",
            county="Merseyside",
            website="https://www.thebeatles.com/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://upload.wikimedia.org/wikipedia/commons/0/0d/The_Fabs.JPG",
        )

        artist2 = Artist(
            name="The Rolling Stones",
            genres=["Rock", "Blues"],
            city="London",
            county="Greater London",
            website="https://www.rollingstones.com/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://upload.wikimedia.org/wikipedia/commons/e/ef/The_Rolling_Stones_1965.JPG",
        )

        artist3 = Artist(
            name="Queen",
            genres=["Rock", "Pop", "Opera Rock"],
            city="London",
            county="Greater London",
            website="https://www.queenonline.com/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://upload.wikimedia.org/wikipedia/commons/f/f2/Queen_performing_in_New_Haven%2C_CT%2C_November_1977.png",
        )

        artist4 = Artist(
            name="Led Zeppelin",
            genres=["Hard Rock", "Heavy Metal"],
            city="London",
            county="Greater London",
            website="https://www.ledzeppelin.com/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://upload.wikimedia.org/wikipedia/commons/d/df/Led_Zeppelin_1977.jpg",
        )

        artist5 = Artist(
            name="Coldplay",
            genres=["Alternative Rock", "Pop Rock"],
            city="London",
            county="Greater London",
            website="https://www.coldplay.com/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://upload.wikimedia.org/wikipedia/commons/d/db/Coldplay_performing_in_2017.jpg",
        )

        db.session.add_all([artist1, artist2, artist3, artist4, artist5])
        db.session.commit()

    # # Create sample shows
    # show1 = Show(artist_id=1, venue_id=1, start_time=datetime(2023, 5, 21, 21, 30))
    # show2 = Show(artist_id=2, venue_id=2, start_time=datetime(2023, 6, 15, 20, 00))

    # Add to session and commit
    db.session.commit()
    print("Seed data added successfully!")
