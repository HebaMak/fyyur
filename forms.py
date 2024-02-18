from datetime import datetime
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL
import re
from enums import Genre, State

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

def is_valid_phone(number):
    regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})
    

class VenueForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL()]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[DataRequired(), URL()]
    )
    website_link = StringField(
        'website_link', validators=[DataRequired(), URL()]
    )
    seeking_talent =  BooleanField( 'seeking_talent', validators=[DataRequired()])

    seeking_description = StringField(
        'seeking_description', validators=[DataRequired()]
    )
    
    def validate_phone(self, field):
        if not is_valid_phone(field.data):
            raise validationError('Invalid phone.')

    def validate_genres(self, field):
        if not set(field.data).issubset(dict(Genre.choices()).keys()):
            raise validationError('Invalid genres.')
    
    def validate_state(self, field):
        if field.data not in dict(state.choices()).keys():
            raise validationError('Invalid state.')
    
    def validate(self, **kwargs):
    return super(VenueForm, self).validate(**kwargs)
    
    
    

class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[DataRequired(), URL()]
    )

    website_link = StringField(
        'website_link', validators=[DataRequired(), URL()]
    )

    seeking_venue = BooleanField( 'seeking_venue', validators=[DataRequired()])
    seeking_description = StringField(
        'seeking_description', validators=[DataRequired()] 
    )
    
    def validate_phone(self, field):
        if not is_valid_phone(field.data):
            raise validationError('Invalid phone.')

    def validate_genres(self, field):
        if not set(field.data).issubset(dict(Genre.choices()).keys()):
            raise validationError('Invalid genres.')
    
    def validate_state(self, field):
        if field.data not in dict(state.choices()).keys():
            raise validationError('Invalid state.')
    
    def validate(self, **kwargs):
    return super(ArtistForm, self).validate(**kwargs)

