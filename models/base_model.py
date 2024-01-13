#!/usr/bin/python3
""" This is the base module for Airbnb project """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ This is the base class """
    def __init__(self, *args, **kwargs):
        """ This is the constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__setattr__(key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ This is the instance representation method """
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ This method update the updated_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def __setattr__(self, name, value):
        """ This override __setattr__ method """
        if name != "updated_at":
            self.updated_at = datetime.now()
        super().__setattr__(name, value)

    def to_dict(self):
        """ This returns dictionary of instance """
        instance_dic = self.__dict__.copy()
        instance_dic["__class__"] = self.__class__.__name__
        instance_dic['created_at'] = self.created_at.isoformat()
        instance_dic['updated_at'] = self.updated_at.isoformat()
        return instance_dic
