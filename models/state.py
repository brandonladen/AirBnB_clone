#!/usr/bin/python3
"""Defines state class that inherits from base_model module"""

from models.base_model import BaseModel

class State(BaseModel):
    """is a child class of BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)