import json
"""File storage module"""


class FileStorage:
    __file_path = "file.json"
    __objects = None

    def new(self, obj):
        self.__objects[obj['__class__']+"."+obj.id] = obj 
    def all(self):
        return self.__objects
    def save(self):
        with open("file.json", "a") as f:
            json.dump(self.__objects,self.__file_path)
    def reload(self):
        with open("file.json","r") as f:
            self.__objects = json.load(f)
if __name__ == "__main__":
    file_storage = FileStorage()
    print(file_storage.__objects)
