class Building:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def setName(self, name):
        self.name = name

    def addRoom(self, room):
        self.rooms.append(room)

class Room:
    def __init__(self, name):
        self.name = name
        self.items = []

    def setName(self, name):
        self.name = name

class Item:
    def __init__(self, name):
        self.name = name
        self.done = False

    def setName(self, name):
        self.name = name
