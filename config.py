import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# Database URI
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/fyyur'

# I used the material provided in this course to build my code
# I used ChatGpt to understand some pieces