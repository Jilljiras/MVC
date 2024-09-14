import json
from model.cow import Cow

class Database:
    def __init__(self, file_path):
        self.file_path = file_path
        self.cows = []
        self.load()

    def load(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read()
                self.cows = [Cow(**item) for item in json.loads(data)]
        except FileNotFoundError:
            self.cows = []

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump([cow.__dict__ for cow in self.cows], file, indent=4)

    def get_cow(self, cow_id):
        for cow in self.cows:
            if cow.id == cow_id:
                return cow
        return None

    def add_cow(self, cow):
        existing_cow = self.get_cow(cow.id)
        if existing_cow:
            self.cows.remove(existing_cow)
        self.cows.append(cow)
        self.save()
