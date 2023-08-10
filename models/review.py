#!/usr/bin/python3
"""Defines review module that inherits from base_model module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Is a child class of BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)