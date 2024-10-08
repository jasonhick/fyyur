from datetime import datetime

from flask import (
    Blueprint,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

from app import db
from app.forms import VenueForm
from app.models import Artist, Show, Venue
from utils.form_utils import flash_form_errors

venues_bp = Blueprint("venues", __name__)


# ----------------------------------------------------------------------------#
# All venues controller - venues.all_venues
# ----------------------------------------------------------------------------#
@venues_bp.route("/")
def all_venues():
    # Query all venues and group them by city and county
    venues = (
        db.session.query(Venue.city, Venue.county)
        .distinct()
        .order_by("county", "city")
        .all()
    )
    data = []

    for venue in venues:
        city_venues = Venue.query.filter_by(
            city=venue.city, county=venue.county
        ).all()
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

        data.append(
            {"city": venue.city, "county": venue.county, "venues": venue_data}
        )

    return render_template("pages/venues.html", areas=data)


# ----------------------------------------------------------------------------#
# Venues search controller - venues.search_venues
# ----------------------------------------------------------------------------#
@venues_bp.route("/search", methods=["POST"])
def search_venues():
    search_term = request.form.get("search_term", "")
    venues = Venue.query.filter(
        db.or_(
            Venue.name.ilike(f"%{search_term}%"),
            Venue.city.ilike(f"%{search_term}%"),
            Venue.county.ilike(f"%{search_term}%"),
        )
    ).all()

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
    shows = (
        db.session.query(Show)
        .join(Artist)
        .filter(Show.venue_id == venue_id)
        .all()
    )

    past_shows = []
    upcoming_shows = []

    for show in shows:
        show_info = {
            "artist_id": show.artist_id,
            "artist_name": show.artist.name,
            "artist_image_link": show.artist.image_link,
            "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        if show.start_time < datetime.now():
            past_shows.append(show_info)
        else:
            upcoming_shows.append(show_info)

    venue = Venue.query.get(venue_id)
    data = venue.__dict__
    data["past_shows"] = past_shows
    data["upcoming_shows"] = upcoming_shows
    data["past_shows_count"] = len(past_shows)
    data["upcoming_shows_count"] = len(upcoming_shows)

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
    form = VenueForm()
    venue = Venue()

    if form.validate_on_submit():
        try:
            form.populate_obj(venue)
            db.session.add(venue)
            db.session.commit()
            flash(f"Venue {venue.name} was successfully listed!")
            return redirect(url_for("venues.show_venue", venue_id=venue.id))

        except Exception as e:
            db.session.rollback()
            flash(
                f"An error occurred. Venue {form.name.data} could not be listed. Error: {str(e)}"
            )
    else:
        flash_form_errors(form)
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
            return (
                jsonify({"success": False, "message": "Venue not found."}),
                404,
            )
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
#  Edit Venue POST handler - venues.edit_venue_submission
#  ----------------------------------------------------------------
@venues_bp.route("/<int:venue_id>/edit", methods=["POST"])
def edit_venue_submission(venue_id):
    form = VenueForm()
    venue = Venue.query.get_or_404(venue_id)

    if form.validate_on_submit():
        try:
            form.populate_obj(venue)
            db.session.commit()
            flash(f"Venue {venue.name} was successfully updated!")
        except Exception as e:
            db.session.rollback()
            flash(
                f"An error occurred. Venue {venue.name} could not be updated."
            )
            print(f"Error: {str(e)}")
        finally:
            db.session.close()
    else:
        flash_form_errors(form)

    return redirect(url_for("venues.show_venue", venue_id=venue_id))
