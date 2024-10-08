from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.forms import ArtistForm
from app.models import Artist, Show, Venue
from utils.form_utils import flash_form_errors

artists_bp = Blueprint("artists", __name__)


# ----------------------------------------------------------------------------#
# All artists controller - artists.all_artists
# ----------------------------------------------------------------------------#
@artists_bp.route("/")
def all_artists():
    # Query all artists from the database
    data = Artist.query.order_by(Artist.name).all()
    return render_template("pages/artists.html", artists=data)


# ----------------------------------------------------------------------------#
# Artists search controller - artists.search_artists
# ----------------------------------------------------------------------------#
@artists_bp.route("/search", methods=["POST"])
def search_artists():
    search_term = request.form.get("search_term", "")
    artists = Artist.query.filter(Artist.name.ilike(f"%{search_term}%")).all()
    response = {
        "count": len(artists),
        "data": artists,
    }

    return render_template(
        "pages/search_artists.html",
        results=response,
        search_term=request.form.get("search_term", ""),
    )


# ----------------------------------------------------------------------------#
# Artist detail controller - artists.show_artist
# ----------------------------------------------------------------------------#
@artists_bp.route("/<int:artist_id>")
def show_artist(artist_id):
    artist = Artist.query.get(artist_id)

    past_shows = (
        db.session.query(Show)
        .join(Venue)
        .filter(Show.artist_id == artist_id, Show.start_time < datetime.now())
        .all()
    )

    upcoming_shows = (
        db.session.query(Show)
        .join(Venue)
        .filter(Show.artist_id == artist_id, Show.start_time >= datetime.now())
        .all()
    )

    def format_shows(shows):
        return [
            {
                "venue_id": show.venue_id,
                "venue_name": show.venue.name,
                "venue_image_link": show.venue.image_link,
                "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for show in shows
        ]

    data = {
        **artist.__dict__,
        "past_shows": format_shows(past_shows),
        "upcoming_shows": format_shows(upcoming_shows),
        "past_shows_count": len(past_shows),
        "upcoming_shows_count": len(upcoming_shows),
    }

    return render_template("pages/show_artist.html", artist=artist)


# ----------------------------------------------------------------------------#
# Artist Create Form - artists.create_artist_form
# ----------------------------------------------------------------------------#
@artists_bp.route("/create", methods=["GET"])
def create_artist_form():
    form = ArtistForm()
    return render_template("forms/new_artist.html", form=form)


# ----------------------------------------------------------------------------#
# Artist Create POST handler - artists.create_artist_submission
# ----------------------------------------------------------------------------#
@artists_bp.route("/create", methods=["POST"])
def create_artist_submission():
    form = ArtistForm()
    artist = Artist()

    if form.validate_on_submit():
        try:
            form.populate_obj(artist)
            db.session.add(artist)
            db.session.commit()
            flash(f"Artist {artist.name} was successfully listed!")
            return redirect(url_for("artists.show_artist", artist_id=artist.id))

        except Exception as e:
            db.session.rollback()
            flash(
                f"An error occurred. Artist {form.name.data} could not be listed. Error: {str(e)}"
            )
    else:
        flash_form_errors(form)
        return render_template("pages/home.html")


# ----------------------------------------------------------------------------#
# Edit Artist Form - artists.edit_artist
# ----------------------------------------------------------------------------#
@artists_bp.route("/<int:artist_id>/edit", methods=["GET"])
def edit_artist(artist_id):
    form = ArtistForm()

    # Fetch the artist from the database using the artist_id
    artist = Artist.query.get(artist_id)

    if artist:
        # Populate the form with values from the fetched artist
        form.process(obj=artist)
    else:
        flash("Artist not found.", "error")
        return redirect(url_for("artists.all_artists"))

    return render_template("forms/edit_artist.html", form=form, artist=artist)


# ----------------------------------------------------------------------------#
# Edit Artist POST handler - artists.edit_artist_submission
# ----------------------------------------------------------------------------#
@artists_bp.route("/<int:artist_id>/edit", methods=["POST"])
def edit_artist_submission(artist_id):
    form = ArtistForm()
    artist = Artist.query.get_or_404(artist_id)

    if form.validate_on_submit():
        try:
            form.populate_obj(artist)
            db.session.commit()
            flash(f"Artist {artist.name} was successfully updated!")
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred. Artist {artist.name} could not be updated.")
            print(f"Error: {str(e)}")
        finally:
            db.session.close()
    else:
        flash_form_errors(form)

    return redirect(url_for("artists.show_artist", artist_id=artist_id))
