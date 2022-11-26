#!/usr/bin/env python3

"""BaseModel class for util purpose."""


import uuid
from datetime import datetime, date
from models import storage


class BaseModel:
    """Base module class."""

    def __init__(self, *args, **kwargs):
        """Intalization for BaseModelClass."""
        if kwargs is None or len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self.to_dict())
        else:
            for x in kwargs.keys():
                if x != '__class__':
                    if x == "created_at" or x == "updated_at":
                        setattr(self, x, datetime.strptime(
                            kwargs[x], "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, x, kwargs[x])

    def to_dict(self):
        """Convert datetime to string time format."""
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
        storage.save()

    def __str__(self):
        """Return string format to print."""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))


if __name__ == "__main__":
    all_objs = storage.all()
    print("-- Reloaded Objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
    new_model = BaseModel()
    new_model.name = "mikias"
    new_model.number = 89
    new_model.save()
    print(new_model)
