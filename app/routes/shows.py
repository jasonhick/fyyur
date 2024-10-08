from flask import Blueprint, flash, render_template, request

from app import db
from app.forms import *
from app.models import Artist, Show, Venue

shows_bp = Blueprint("shows", __name__)


# ----------------------------------------------------------------------------#
# Shows list controller - shows.all_shows
# ----------------------------------------------------------------------------#
@shows_bp.route("/")
def all_shows():
    # displays list of shows at /shows
    # join the artist and venue tables

    data = (
        db.session.query(Show)
        .join(Artist)
        .join(Venue)
        .with_entities(
            Show.id,
            Show.start_time,
            Artist.id.label("artist_id"),
            Artist.name.label("artist_name"),
            Artist.image_link.label("artist_image_link"),
            Venue.id.label("venue_id"),
            Venue.name.label("venue_name"),
        )
        .all()
    )
    return render_template("pages/shows.html", shows=data)


# ----------------------------------------------------------------------------#
# Create Shows Form - shows.create_shows
# ----------------------------------------------------------------------------#
@shows_bp.route("/create")
def create_shows():
    # renders form. do not touch.
    form = ShowForm()
    return render_template("forms/new_show.html", form=form)


# ----------------------------------------------------------------------------#
# Create Shows POST handler - shows.create_show_submission
# ----------------------------------------------------------------------------#
@shows_bp.route("/create", methods=["POST"])
def create_show_submission():
    form = ShowForm(request.form)
    if form.validate():
        new_show = Show(
            artist_id=form.artist_id.data,
            venue_id=form.venue_id.data,
            start_time=form.start_time.data,
        )
        db.session.add(new_show)
        db.session.commit()
        flash("Show was successfully listed!")
    else:
        flash("An error occurred. Show could not be listed.")
    return render_template("pages/home.html")
