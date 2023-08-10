#!/usr/bin/python3
"""defines a class city"""


from models.base_model import BaseModel

class city(BaseModel):
    """child class of the BaseModel
    it has 2 attributes - state id and name of the city"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init"""
        super().__init__(*args, **kwargs)