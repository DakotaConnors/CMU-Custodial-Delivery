import Location as loc
import ReadInventory
import random

if __name__ == '__main__':
    Buildings = []  #Both Used in
    Inventory = []  #MainApp and Network

    everythingWorks = True
    whatIsBroken = ''

    print('Testing these functions:\n')


    print('Add Buildings')
    for i in range(5):
        buildingName = 'Test Building' + str(i+1)
        Buildings.append(loc.Building(buildingName))
    print(' -',len(Buildings), 'Buildings Added')
    if len(Buildings) == 0:
        everythingWorks = False
        whatIsBroken += 'Adding Buildings is broken\n'

    print('Changing Building Name')
    randomInt = random.randint(0,4)
    Buildings[randomInt].setName('RandomName')
    for i in range(5):
        print(' -',Buildings[i].name)

    foundChangedName = False
    for building in Buildings:
        if building.name == 'RandomName': foundChangedName = True
    if not(foundChangedName):
        everythingWorks = False
        whatIsBroken += 'Building.setName is broken\n'

    print('Adding Rooms')
    for i in range(5):
        roomName = 'TestRoom' + str(i+1)
        Buildings[0].addRoom(loc.Room(roomName))
    print(' -',len(Buildings[0].rooms), 'Rooms Added to', Buildings[0].name)
    if len(Buildings[0].rooms) == 0:
        everythingWorks = False
        whatIsBroken += 'Buildings.addRoom is broken\n'

    print('Changing Room Name')
    randomInt = random.randint(0,4)
    Buildings[0].rooms[randomInt].setName('RandomName')

    foundChangedName = False
    for room in Buildings[0].rooms:
        if room.name == 'RandomName': foundChangedName = True
    if not(foundChangedName):
        everythingWorks = False
        whatIsBroken += 'Room.setName is broken\n'

    print('Reading Inventory')
    Inventory = ReadInventory.readInventory()
    print(' - ', len(Inventory), 'Items in the inventory')
    if len(Inventory) == 0:
        everythingWorks = False
        whatIsBroken += 'ReadInventory.readInventory is broken\n'

    if everythingWorks: print('EVERYTHING WORKS!')
    else:
        print(whatIsBroken)
