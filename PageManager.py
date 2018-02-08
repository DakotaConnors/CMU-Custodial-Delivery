Labels = []

class PageManager:
    def __init__(self):
        pass

    def ChangePage(self, PageNumber, Buildings, Currents):
        Labels = []
        AvailableButtons = []
        for i in range(20):
            Labels.append('')
        if PageNumber == 0.0: #Log In Page
            Labels[0] = 'Log in page'
            Labels[2] = 'Click Log In To Continue'
        elif PageNumber == 1.0: #Home Page
            Labels[0] = 'Welcome to the Home Page'
            Labels[1] = 'What would you like to do?'
            Labels[4] = 'View Buildings'
            Labels[5] = 'Log Out'
            AvailableButtons.append(4)
            AvailableButtons.append(5)
        elif PageNumber == 2.0: #Viewing Buildings
            Labels[0] = 'Viewing CMU Custodial Building List'
            for i in range(len(Buildings)):
                Labels[2+i] = Buildings[i].name
            Labels[len(Buildings) + 4] = 'What would you like to do?'
            Labels[len(Buildings) + 5] = 'View Building'
            Labels[len(Buildings) + 6] = 'Add Building'
            Labels[len(Buildings) + 7] = 'Delete Building'
            Labels[len(Buildings) + 8] = 'Edit Building'
            Labels[len(Buildings) + 9] = 'Back'
            AvailableButtons.append(len(Buildings) + 5)
            AvailableButtons.append(len(Buildings) + 6)
            AvailableButtons.append(len(Buildings) + 7)
            AvailableButtons.append(len(Buildings) + 8)
            AvailableButtons.append(len(Buildings) + 9)
        elif PageNumber == 2.1: #Choosing a building to view
            Labels[0] = 'Which Building would you like to view?'
            for i in range(len(Buildings)):
                Labels[2+i] = Buildings[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 2.2: #adding a building
            Labels[0] = 'What would you like to name this new Building?'
            AvailableButtons.append(3)

        elif PageNumber == 2.3: #deleting a building
            Labels[0] = 'Which Building would you like to remove from this list?'
            for i in range(len(Buildings)):
                Labels[2+i] = Buildings[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 2.4: #asking which building to edit
            Labels[0] = 'Which Building would you like to edit?'
            for i in range(len(Buildings)):
                Labels[2+i] = Buildings[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 2.5: #editing building name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].name)
            AvailableButtons.append(3)

        elif PageNumber == 3.0: #Viewing Buildings
            Labels[0] = ('Viewing ' + Buildings[Currents[0]].name + "'" + 's rooms')
            for i in range(len(Buildings[Currents[0]].rooms)):
                Labels[2+i] = Buildings[Currents[0]].rooms[i].name
            Labels[len(Buildings[Currents[0]].rooms) + 4] = 'What would you like to do?'
            Labels[len(Buildings[Currents[0]].rooms) + 5] = 'View Room'
            Labels[len(Buildings[Currents[0]].rooms) + 6] = 'Add Room'
            Labels[len(Buildings[Currents[0]].rooms) + 7] = 'Delete Room'
            Labels[len(Buildings[Currents[0]].rooms) + 8] = 'Edit Room'
            Labels[len(Buildings[Currents[0]].rooms) + 9] = 'Back'
            AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 5)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 6)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 7)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 8)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 9)

        elif PageNumber == 3.1: #asking which room to view
            for i in range(len(Buildings[Currents[0]].rooms)):
                Labels[2+i] = Buildings[Currents[0]].rooms[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 3.2: #adding a room
            Labels[0] = 'What would you like to name this new Room?'
            AvailableButtons.append(3)

        elif PageNumber == 3.3: #deleting a room
            Labels[0] = 'Which Room would you like to remove from this list?'
            for i in range(len(Buildings[Currents[0]].rooms)):
                Labels[2+i] = Buildings[Currents[0]].rooms[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 3.4: #asking which room to edit
            Labels[0] = 'Which Room would you like to edit?'
            for i in range(len(Buildings[Currents[0]].rooms)):
                Labels[2+i] = Buildings[Currents[0]].rooms[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 3.5: #editing room name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].rooms[Currents[1]].name)
            AvailableButtons.append(3)

        elif PageNumber == 4.0: #Viewing items
            Labels[0] = ('Viewing ' + Buildings[Currents[0]].rooms[Currents[1]].name + "'" + 's items')
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i].name
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 4] = 'What would you like to do?'
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 5] = 'View Item'
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 6] = 'Add Item'
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 7] = 'Delete Item'
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 8] = 'Edit Item'
            Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 9] = 'Back'
            AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 5)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 6)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 7)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 8)
            AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 9)

        elif PageNumber == 4.1: #asking which item to view
            for i in range(len(Buildings[Currents[0]].rooms)):
                Labels[2+i] = Buildings[Currents[0]].rooms[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 4.2: #adding a item
            Labels[0] = 'What would you like to name this new Item?'
            AvailableButtons.append(3)

        elif PageNumber == 4.3: #deleting a item
            Labels[0] = 'Which Item would you like to remove from this list?'
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 4.4: #asking which item to edit
            Labels[0] = 'Which Item would you like to edit?'
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i].name
                AvailableButtons.append(2+i)

        elif PageNumber == 4.5: #editing item name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].name)
            AvailableButtons.append(3)

        return Labels, AvailableButtons
