#!/usr/bin/python3
"""Defines a class place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """child class of the BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    nummber_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)