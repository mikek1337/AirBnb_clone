#!/usr/bin/env python3


import uuid
from datetime import datetime

"""" BaseModel class for util purpose."""


class BaseModel:
    """Base module class."""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts datetime to string time format."""
        copy_dict = dict(self.__dict__)
        copy_dict['__class__'] = self.__class__.__name__
        copy_dict['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        copy_dict['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        return copy_dict

    def save(self):
        """Update update date."""
        self.__dict__['updated_at'] = datetime.now()

    def __str__(self):
        """Return string format to print."""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


if __name__ == "__main__":
    base_model = BaseModel()
    base_model.name = "mikias"
    base_model.my_number = 100

    base_model.save()

    dic_json = base_model.to_dict()
    print(dic_json)
    for key in dic_json.keys():
        print("\t{}: ({}) - {}".format(key,
              type(dic_json[key]), dic_json[key]))
