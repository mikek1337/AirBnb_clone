"""File storage module"""


class FileStorage:
    __file_path = "file.json"
    __objects = None

    def __init__(self):
        pass


if __name__ == "__main__":
    file_storage = FileStorage()
    print(file_storage.__objects)
