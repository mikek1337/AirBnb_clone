"""File storage module."""

import json


class FileStorage:
    """Storage engine instance."""

    __file_path = "file.json"
    __objects = None

    def new(self, obj):
        self.__objects[obj['__class__']+"."+obj.id] = obj

    def all(self):
        return self.__objects

    def save(self):
        try:
            with open("file.json", "a", errors="ignore") as f:
                json.dump(self.__objects, self.__file_path)
        except OSError as e:
            pass

    def reload(self):
        try:
            with open("file.json", "r", errors="ignore") as f:
                self.__objects = json.load(f)
        except OSError as e:
            pass
