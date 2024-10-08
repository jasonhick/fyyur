from datetime import datetime

from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for

from app import db
from app.forms import VenueForm
from app.models import Show, Venue
from app.models.artist import Artist
from utils.form_utils import flash_form_errors

venues_bp = Blueprint("venues", __name__)


# ----------------------------------------------------------------------------#
# Main venues controller - venues.all_venues
# ----------------------------------------------------------------------------#


@venues_bp.route("/")
def all_venues():
    # Query all venues and group them by city and state
    venues = (
        db.session.query(Venue.city, Venue.state)
        .distinct()
        .order_by("state", "city")
        .all()
    )
    data = []

    for venue in venues:
        city_venues = Venue.query.filter_by(city=venue.city, state=venue.state).all()
        venue_data = []

        for v in city_venues:
            venue_data.append(
                {
                    "id": v.id,
                    "name": v.name,
                    "num_upcoming_shows": db.session.query(Show)
                    .filter(Show.venue_id == v.id)
                    .count(),
                }
            )

        data.append({"city": venue.city, "state": venue.state, "venues": venue_data})

    return render_template("pages/venues.html", areas=data)


# ----------------------------------------------------------------------------#
# Venues search controller - venues.search_venues
# ----------------------------------------------------------------------------#


@venues_bp.route("/search", methods=["POST"])
def search_venues():
    search_term = request.form.get("search_term", "")
    venues = Venue.query.filter(Venue.name.ilike(f"%{search_term}%")).all()
    response = {
        "count": len(venues),
        "data": venues,
    }
    return render_template(
        "pages/search_venues.html", results=response, search_term=search_term
    )


# ----------------------------------------------------------------------------#
# Venue detail controller - venues.show_venue
# ----------------------------------------------------------------------------#


@venues_bp.route("/<int:venue_id>")
def show_venue(venue_id):
    # shows the venue page with the given venue_id
    venue = Venue.query.get(venue_id)

    past_shows = (
        db.session.query(Show)
        .join(Artist)
        .filter(Show.venue_id == venue_id, Show.start_time < datetime.now())
        .all()
    )

    upcoming_shows = (
        db.session.query(Show)
        .join(Artist)
        .filter(Show.venue_id == venue_id, Show.start_time >= datetime.now())
        .all()
    )

    data = {
        "id": venue.id,
        "name": venue.name,
        "genres": venue.genres,
        "address": venue.address,
        "city": venue.city,
        "state": venue.state,
        "phone": venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link,
        "past_shows": [
            {
                "artist_id": show.artist_id,
                "artist_name": show.artist.name,
                "artist_image_link": show.artist.image_link,
                "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for show in past_shows
        ],
        "upcoming_shows": [
            {
                "artist_id": show.artist_id,
                "artist_name": show.artist.name,
                "artist_image_link": show.artist.image_link,
                "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for show in upcoming_shows
        ],
        "past_shows_count": len(past_shows),
        "upcoming_shows_count": len(upcoming_shows),
    }

    return render_template("pages/show_venue.html", venue=data)


#  ----------------------------------------------------------------
#  Create Venue Form - venues.create_venue_form
#  ----------------------------------------------------------------


@venues_bp.route("/create", methods=["GET"])
def create_venue_form():
    form = VenueForm()
    return render_template("forms/new_venue.html", form=form)


#  ----------------------------------------------------------------
#  Create Venue POST handler - venues.create_venue_submission
#  ----------------------------------------------------------------


@venues_bp.route("/create", methods=["POST"])
def create_venue_submission():
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    # on successful db insert, flash success
    flash("Venue " + request.form["name"] + " was successfully listed!")
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return render_template("pages/home.html")


#  ----------------------------------------------------------------
#  Delete Venue - venues.delete_venue
#  ----------------------------------------------------------------


@venues_bp.route("/<venue_id>", methods=["DELETE"])
def delete_venue(venue_id):
    try:
        venue = Venue.query.get(venue_id)
        if venue:
            db.session.delete(venue)
            db.session.commit()
            flash(f"Venue {venue.name} was successfully deleted.", "success")
            return (
                jsonify(
                    {
                        "success": True,
                        "message": f"Venue {venue.name} was successfully deleted.",
                    }
                ),
                200,
            )
        else:
            flash("Venue not found.", "error")
            return jsonify({"success": False, "message": "Venue not found."}), 404
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred. Venue could not be deleted.", "error")
        return (
            jsonify(
                {
                    "success": False,
                    "message": f"An error occurred. Venue could not be deleted. Error: {str(e)}",
                }
            ),
            500,
        )
    finally:
        db.session.close()


#  ----------------------------------------------------------------
#  Edit Venue Form - venues.edit_venue
#  ----------------------------------------------------------------
@venues_bp.route("/<venue_id>/edit", methods=["GET"])
def edit_venue(venue_id):
    form = VenueForm()

    # Fetch the venue from the database using the venue_id
    venue = Venue.query.get(venue_id)

    if venue:
        # Populate the form with values from the fetched venue
        form.process(obj=venue)
    else:
        flash("Venue not found.", "error")
        return redirect(url_for("venues.all_venues"))

    return render_template("forms/edit_venue.html", form=form, venue=venue)


#  ----------------------------------------------------------------
#  Update Venue POST handler - venues.update_venue
#  ----------------------------------------------------------------


@venues_bp.route("/<int:venue_id>/edit", methods=["POST"])
def update_venue(venue_id):
    form = VenueForm()
    venue = Venue.query.get_or_404(venue_id)

    if form.validate_on_submit():
        try:
            form.populate_obj(venue)
            db.session.commit()
            flash(f"Venue {venue.name} was successfully updated!")
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred. Venue {venue.name} could not be updated.")
            print(f"Error: {str(e)}")
        finally:
            db.session.close()
    else:
        flash_form_errors(form)

    return redirect(url_for("venues.show_venue", venue_id=venue_id))
