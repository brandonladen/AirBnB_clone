#!/usr/bin/python3
"""Defines FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
        This class serializes instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        dict_attrs = obj.to_dict()
        new_key = "{}.{}".format(dict_attrs["__class__"], dict_attrs["id"])
        self.__objects[new_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = {}
                if content != "":
                    dict_from_file = json.loads(content)  # type = dict

                for file_key, dict_obj in dict_from_file.items():
                    # if the key_file is not in the storage.keys()
                    # create a new instance and pass it argument and kwargs
                    if file_key not in FileStorage.__objects.keys():
                        className = dict_obj["__class__"]
                        newInst = eval("{}(**dict_obj)".format(className))
                        self.new(newInst)
        except FileNotFoundError:
            pass
