"""File storage module."""

import json


class FileStorage:
    """Storage engine instance."""

    __file_path = "file.json"
    __objects = dict()

    def new(self, obj):
        """Assigns new object to __objects."""
        if obj != None:
            obj_key = ''
            obj_key = obj['__class__']+'.'+obj['id']
            self.__class__.__objects[obj_key] = obj

    def all(self):
        """Returns all the objects saved."""
        return self.__class__.__objects

    def save(self):
        """Saves the new object to file"""
        try:
            with open(self.__file_path, "w", errors="ignore") as f:
                json.dump(self.__class__.__objects, f)
        except OSError as e:
            pass

    def reload(self):
        """Loads object from file."""
        try:
            with open("file.json", "r", errors="ignore") as f:
                self.__class__.__objects = json.load(f)
        except OSError as e:
            pass
