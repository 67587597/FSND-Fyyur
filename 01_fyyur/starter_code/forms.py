from datetime import datetime
import enum
from enum import Enum
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, FileField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, ValidationError, Regexp, Optional
# from app import app

class Geners(enum.Enum):
  Alternative = 'Alternative'
  Blues = 'Blues'
  Classical = 'Classical'
  Country = 'Country'
  Electronic = 'Electronic'
  Folk = 'Folk'
  Funk = 'Funk'
  HipHop = 'Hip-Hop '
  HeavyMetal = 'Heavy Metal'
  Instrumental = 'Instrumental'
  Jazz = 'Jazz'
  MusicalTheatre = 'Musical Theatre'
  Pop = 'Pop'
  Punk = 'Punk'
  RB = 'R&B'
  Reggae = 'Reggae'
  RocknRoll = 'Rock n Roll'
  Soul = 'Soul'
  Other = 'Other'

def check_Enum_value():
    # geners= [g.value for g in Geners]
    enumIter = [g.value for g in Geners]
    messgae = f'<Allowed values: {enumIter}>'
    
    def _check_Enum_value(form,field):
      error = True
      print(field.data)
      for c in field.data:
        if c in enumIter:
          pass
        else:
          error = False
      if error:
        raise ValidationError(messgae)

def check_allowed_image(form, field):
    if field.raw_data is not None:
      if field.raw_data[0] is not None:
        filename = field.raw_data[0].filename
    print(filename)
    if filename is not None: 
      if not "." in filename:
        raise ValidationError('select file')
    # Split the extension from the filename
    if filename is not None:
      ext = filename.rsplit(".", 1)[1]
    #   print('filename xxxxxxxxxxxxxxxxxxxxxxxxx')

      ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF"]
      # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
      if ext.upper() in ALLOWED_IMAGE_EXTENSIONS:
        # print('filename ttttttttttttttttttttttttttttt')
        return True
      else:
        raise ValidationError('Not Allowed File Extension')
    else:
        return True

    
# Geners = Enum(
#     value='Gener',
#     names=[
#     ('Alternative','Alternative')
#     ('Blues', 'Blues')
#     ('Classical', 'Classical')
#     ('Country', 'Country')
#     ('Electronic',  'Electronic')
#     ('Folk', 'Folk')
#     ('Funk', 'Funk')
#     ('Hip-Hop', 'Hip-Hop')
#     ('Heavy Metal', 'Heavy Metal')
#     # Instrumental = 10
#     # Jazz = 11
#     # 'Musical Theatre' = 12
#     # Pop = 13
#     # Punk = 14
#     # R&B = 15
#     # Reggae = 16
#     # 'Rock n Roll' = 17
#     # Soul = 18
#     # Other = 19
#     ])

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )
    



class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[Regexp("^[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}?")]
    )
    # image_link = StringField(
    #     'image_link'
    # )
    # use suggested solution in https://knowledge.udacity.com/questions/61746
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices= [( g.value, g.value) for g in Geners]
        # [
        #     ('Alternative', 'Alternative'),
        #     ('Blues', 'Blues'),
        #     ('Classical', 'Classical'),
        #     ('Country', 'Country'),
        #     ('Electronic', 'Electronic'),
        #     ('Folk', 'Folk'),
        #     ('Funk', 'Funk'),
        #     ('Hip-Hop', 'Hip-Hop'),
        #     ('Heavy Metal', 'Heavy Metal'),
        #     ('Instrumental', 'Instrumental'),
        #     ('Jazz', 'Jazz'),
        #     ('Musical Theatre', 'Musical Theatre'),
        #     ('Pop', 'Pop'),
        #     ('Punk', 'Punk'),
        #     ('R&B', 'R&B'),
        #     ('Reggae', 'Reggae'),
        #     ('Rock n Roll', 'Rock n Roll'),
        #     ('Soul', 'Soul'),
        #     ('Other', 'Other'),
        # ]
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    # using reference https://pythonise.com/series/learning-flask/flask-uploading-files
    image_link = FileField(
        'image_link', validators=[check_allowed_image]
        )
    seeking_talent = BooleanField(
        'seeking_talent'
        )
    seeking_description = StringField(
        'seeking_description'
        )

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[Regexp("^[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}?")]
    )
    # image_link = StringField(
    #     'image_link'
    # )
    genres = SelectMultipleField(
        # TODO implement enum restriction 
        'genres', validators=[DataRequired()],
        choices= [( g.value, g.value) for g in Geners]
        # choices=[
        #     ('Alternative', 'Alternative'),
        #     ('Blues', 'Blues'),
        #     ('Classical', 'Classical'),
        #     ('Country', 'Country'),
        #     ('Electronic', 'Electronic'),
        #     ('Folk', 'Folk'),
        #     ('Funk', 'Funk'),
        #     ('Hip-Hop', 'Hip-Hop'),
        #     ('Heavy Metal', 'Heavy Metal'),
        #     ('Instrumental', 'Instrumental'),
        #     ('Jazz', 'Jazz'),
        #     ('Musical Theatre', 'Musical Theatre'),
        #     ('Pop', 'Pop'),
        #     ('Punk', 'Punk'),
        #     ('R&B', 'R&B'),
        #     ('Reggae', 'Reggae'),
        #     ('Rock n Roll', 'Rock n Roll'),
        #     ('Soul', 'Soul'),
        #     ('Other', 'Other'),
        # ]
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    # using reference https://pythonise.com/series/learning-flask/flask-uploading-files
    image_link = FileField(
        'image_link', validators=[check_allowed_image]
        )
    seeking_venue = BooleanField(
        'seeking_venue'
        )
    seeking_description = StringField(
        'seeking_description'
        )
    

# TODO IMPLEMENT NEW ARTIST FORM AND NEW SHOW FORM
