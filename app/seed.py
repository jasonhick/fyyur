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
            website_link="https://www.academymusicgroup.com/o2academybrixton/",
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
            website_link="https://www.rock-city.co.uk/",
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
            website_link="https://www.liverpoolguild.org/",
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
            website_link="https://www.clwb.net/",
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
            website_link="https://heaven-live.co.uk/",
            facebook_link="https://www.facebook.com/HeavenNightclub/",
            seeking_talent=False,
            seeking_description="",
            image_link="https://thatsup.co.uk/content/img/place/h/e/heaven-2.jpg",
        )

        db.session.add_all([venue1, venue2, venue3, venue4, venue5])
        db.session.commit()
        print("Venue data added successfully!")

    if Artist.query.first():
        print("Artist data already exists. Skipping...")
    else:
        # Create sample artists
        artist1 = Artist(
            name="Coldplay",
            city="London",
            county="Greater London",
            phone="+44 20 7890 1234",
            genres=["Rock n Roll"],
            facebook_link="https://www.facebook.com/coldplay",
            image_link="https://upload.wikimedia.org/wikipedia/commons/2/2e/ColdplayBBC071221_%28cropped%29.jpg",
            seeking_talent=False,
            seeking_venue=False,
            seeking_description="",
            website_link="https://www.coldplay.com",
        )

        artist2 = Artist(
            name="Led Zeppelin",
            city="London",
            county="Greater London",
            phone="+44 20 8901 4567",
            genres=["Heavy Metal"],
            facebook_link="https://www.facebook.com/ledzeppelin",
            image_link="https://static.independent.co.uk/s3fs-public/thumbnails/image/2014/03/13/14/led-zeppelin2.jpg",
            seeking_talent=False,
            seeking_venue=False,
            seeking_description="",
            website_link="https://www.ledzeppelin.com",
        )

        artist3 = Artist(
            name="Queen",
            city="London",
            county="Greater London",
            phone="+44 20 2233 4455",
            genres=["Pop"],
            facebook_link="https://www.facebook.com/Queen/",
            image_link="https://lookingglass.montroseschool.org/wp-content/uploads/queen.jpeg",
            seeking_talent=False,
            seeking_venue=False,
            seeking_description="",
            website_link="https://www.queenonline.com",
        )

        artist4 = Artist(
            name="The Beatles",
            city="Liverpool",
            county="Merseyside",
            phone="+44 151 1234 7890",
            genres=["Pop"],
            facebook_link="https://www.facebook.com/thebeatles/",
            image_link="https://c.files.bbci.co.uk/1260/production/_108240740_beatles-abbeyroad-index-reuters-applecorps.jpg",
            seeking_talent=False,
            seeking_venue=False,
            seeking_description="",
            website_link="https://www.thebeatles.com",
        )

        artist5 = Artist(
            name="The Rolling Stones",
            city="London",
            county="Greater London",
            phone="+44 20 5566 8899",
            genres=["Blues"],
            facebook_link="https://www.facebook.com/therollingstones/",
            image_link="https://ca-times.brightspotcdn.com/dims4/default/9c5c2a3/2147483647/strip/true/crop/6000x4763+0+0/resize/1200x953!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F48%2Ffe%2F6412c05146738e437b2f84953e4b%2Fcredit-mark-seliger-1.jpg",
            seeking_talent=False,
            seeking_venue=False,
            seeking_description="",
            website_link="https://www.rollingstones.com",
        )

        db.session.add_all([artist1, artist2, artist3, artist4, artist5])
        db.session.commit()
        print("Artist data added successfully!")

    if Show.query.first():
        print("Show data already exists. Skipping...")
        return
    else:
        # Create sample shows
        show1 = Show(
            artist_id=1, venue_id=1, start_time=datetime(2024, 11, 21, 21, 30)
        )
        show2 = Show(
            artist_id=2, venue_id=2, start_time=datetime(2024, 11, 21, 20, 00)
        )
        show3 = Show(
            artist_id=3, venue_id=3, start_time=datetime(2024, 11, 21, 20, 00)
        )
        show4 = Show(
            artist_id=4, venue_id=4, start_time=datetime(2023, 11, 21, 20, 00)
        )
        show5 = Show(
            artist_id=5, venue_id=5, start_time=datetime(2023, 11, 21, 20, 00)
        )

        db.session.add_all([show1, show2, show3, show4, show5])
        db.session.commit()
        print("Show data added successfully!")
