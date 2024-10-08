# Fyyur

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Development Setup](#development-setup)
- [Main Files: Project Structure](#main-files-project-structure)

## Introduction

This is project 1 of the Udacity Full Stack Nanodegree.

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.

**IMPORTANT:** Please note that the strucuture of the site has been significantly changed from the original project:

- `app.py` has been renamed to `run.py` and is the main entry point for the application
- `state` is now `county` to match the UK location
- The database has been seeded with UK based artists, venues and shows

## Dependencies

The site was built using the following dependencies.
Please ensure exact versions are installed (where specified) as the original project did not initially work.

- **Python 3.10.0**
- **node 20.17.0**
- **virtualenv** for creating isolated Python environments
- **SQLAlchemy ORM** as our ORM library of choice
- **PostgreSQL** as our database of choice
- **Python3** and **Flask** as our server language and server framework
- **Flask-Migrate** for creating and running schema migrations

## Installation

Install Python dependencies using `pip`:

```bash
pip install virtualenv
pip install SQLAlchemy
pip install psycopg2-binary
pip install Flask
pip install Flask-Migrate
```

## Development Setup

1. **Download the project starter code locally**

```bash
git clone https://github.com/jasonhick/fyyur.git
cd fyyur
```

3. **Initialize and activate a virtualenv:**

```bash
python -m virtualenv env
source env/bin/activate
```

4. **Install the dependencies:**

   The original project did not work, so the exact versions from requirements must be installed:

```bash
pip install -r requirements.txt
```

5. **Install node dependencies:**

```bash
npm install
```

6. **Run the development server:**

Make sure you have setup the database and run the migrations first or the app will not run.
This is because the app will try to seed the database with test data, and it will not work if the database is not set up.

- Ensure the `fyyur` database is created locally
- run `flask db upgrade` from the project root to run the migrations

```bash
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 run.py
```

7. **Verify on the Browser**<br>
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000)

## Main Files: Project Structure

```sh
├── README.md
├── run.py # Main driver of the app.
├── config.py
├── error.log
├── app
│   ├── __init__.py
│   ├── forms.py
│   ├── seed.py
│   ├── models
│   │   ├── artists.py
│   │   ├── shows.py
│   │   ├── venues.py
│   ├── routes
│   │   ├── artists.py
│   │   ├── shows.py
│   │   ├── venues.py
│   ├── static
│   ├── templates
├── migrations
├── utils

```

- Models are located in `app/models`.
- Controllers are located in `app/routes`.
- The web frontend is located in `app/templates/`
- Static assets are located `app/static/`.
- Web forms for creating data are located in `app/forms.py`.

## Stand Out

To make your submission stand out, consider implementing:

- Artist availability.
- Recent Listed Artists and Venues on the homepage.
- Search Artists and Venues by City and State.
