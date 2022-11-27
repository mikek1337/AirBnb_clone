#!/usr/bin/python3

"""Place model."""

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class."""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = ''
    number_bathroom = ''
    max_guest = ''
    price_by_night = ''
    latitude = ''
    longitude = ''
    amenity = ''