#!/usr/bin/python3
"""File storage module."""

import json
import models


class FileStorage:
    """Storage engine instance."""

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Assigns new object to __objects."""
        if obj != None:
            obj_key = ''
            obj_key = str(obj.__class__.__name__) + "." + str(obj.id)
            value = obj
            self.__objects[obj_key] = value

    def all(self):
        """Returns all the objects saved."""
        return self.__objects

    def save(self):
        """Saves the new object to file"""
        rep_obj = {}
        for key, val in self.__objects.items():
            rep_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, "w",  encoding="UTF-8") as f:
            json.dump(rep_obj, f)
       

    def reload(self):
        """Loads object from file."""
        try:
            with open(FileStorage.__file_path, "r", errors="ignore") as f:
                FileStorage.__objects = json.load(f)
                for key, val in self.__objects.items():
                    class_name = val['__class__']
                    class_name = models.classes[class_name]
                    FileStorage.__objects[key] = class_name(**val)
        except OSError as e:
            pass
