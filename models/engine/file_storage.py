#!/usr/bin/python3
""" This Module for storage """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.Amenity import Amenity
from models.review import Review


class FileStorage():
    """ This model to store all instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method return all instances dictionary"""
        return self.__objects

    def new(self, obj):
        """ This method store new obj to the dictionary"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ This method return the json representation of all instances"""
        with open(self.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ This method reload instances from file to the dictionary"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
