#!/usr/bin/python3
"""Defines the class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """is a child class of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)
        