#!/usr/bin/python3
"""Difines BaseModel class"""
import uuid
import datetime
import models


class BaseModel:
    """
        Defines all common attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Constructor of class BaseModel
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)

    def save(self):
        """
            updates the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary
        """
        dict_copy = self.__dict__.copy()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """
            String information of the BaseModel
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)
    