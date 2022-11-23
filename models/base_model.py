#!/usr/bin/env python3
"""Base module."""

import uuid
from datetime import date

"""" BaseModel class for util purpose."""


class BaseModel:
    id = str(uuid.uuid4())
    created_at = date.today()
    updated_at = date.today()

    def __str__(self):
        pass



if __name__ == "__main__":
    base_model = BaseModel()
   
