import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:95149514@localhost:5432/fyyur'
IMAGE_UPLOADS = "C:/Users/sa-95/Downloads/Learning/FSND/FSND-Fyyur/01_fyyur/starter_code/static/img"
ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]