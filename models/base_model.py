#!/usr/bin/env python3
"""Base module."""

import uuid

"""" BaseModel class for util purpose """


class BaseModel:
    id = str(uuid.uuid4())


if __name__ == "__main__":
    base_model = BaseModel()
    print(base_model.id)
