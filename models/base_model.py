#!/usr/bin/python3
"""Difines BaseModel class"""
import uuid
import datetime


class BaseModel:
    """
        Defines all common attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Constructor of class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
            updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return {"my_number": self.my_number, "name": self.name, "updated_at": self.updated_at.isoformat(), "id": self.id, "created_at": self.created_at.isoformat()}

    def __str__(self):
        """
            String information of the BaseModel
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)