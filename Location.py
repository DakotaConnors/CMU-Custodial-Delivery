import datetime

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
        self.fullAmount = 0
        self.lastReplaced = '?'
        self.replacementCycle = []

    def setName(self, name):
        self.name = name

class InventoryItem:
    def __init__(self, _id, name, number):
        self.id = _id
        self.name = name
        self.number = number
