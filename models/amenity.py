#!/usr/bin/python3
"""Defines amenity class that inherits from base_model module"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """is a child of class BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)