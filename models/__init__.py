"""Models package."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City

classes = {
    "BaseModel":BaseModel,
    "User":User,
    "Place":Place,
    "City":City,
    "Review":Review,
    "Amenity":Amenity,
    "State":State
    }
storage = FileStorage()
storage.reload()
