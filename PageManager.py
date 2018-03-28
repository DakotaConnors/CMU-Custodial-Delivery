import Inventory as inv
import Location as loc
import Delivery

Labels = []

class PageManager:
    def __init__(self):
        pass

    def sortBuildingsZtoA(self, Buildings):
        sortedBuildings = sorted(Buildings, key=lambda x: x.name, reverse=True)
        return sortedBuildings

    def sortBuildingsAtoZ(self, Buildings):
        sortedBuildings = sorted(Buildings, key=lambda x: x.name)
        return sortedBuildings


    def ChangePage(self, PageNumber, Buildings, Currents, LinePosition, pendingDeliveries, completedDeliveries):
        Labels = []
        AvailableButtons = []
        labelColors = []
        for i in range(20):
            Labels.append('')
            labelColors.append('')
        if PageNumber == 0.0: #Log In Page
            Labels[0] = 'Log in page'
            Labels[2] = 'Click Log In To Continue'
        elif PageNumber == 1.0: #Home Page
            Labels[0] = 'Welcome to the Home Page'
            Labels[1] = 'What would you like to do?'
            Labels[4] = 'View Buildings'
            Labels[5] = 'View Deliveries'
            Labels[6] = 'Log Out'
            AvailableButtons.append(4)
            AvailableButtons.append(5)
            AvailableButtons.append(6)
        elif PageNumber == 2.0: #Viewing Buildings
            Labels[0] = 'Viewing CMU Custodial Building List'
            for i in range(len(Buildings)):
                if i < 10: Labels[2+i] = Buildings[i+LinePosition].name

            if len(Buildings) <= 10:
                Labels[len(Buildings) + 4] = 'What would you like to do?'
                Labels[len(Buildings) + 5] = 'View Building'
                Labels[len(Buildings) + 6] = 'Add Building'
                Labels[len(Buildings) + 7] = 'Delete Building'
                Labels[len(Buildings) + 8] = 'Edit Building'
                Labels[len(Buildings) + 9] = 'Back'
            else:
                Labels[14] = 'What would you like to do?'
                Labels[15] = 'View Building'
                Labels[16] = 'Add Building'
                Labels[17] = 'Delete Building'
                Labels[18] = 'Edit Building'
                Labels[19] = 'Back'

            for i in range(5):
                if len(Buildings) > 10: AvailableButtons.append(15 + i)
                else: AvailableButtons.append(len(Buildings) + 5 + i)
        elif PageNumber == 2.1: #Choosing a building to view
            Labels[0] = 'Which Building would you like to view?'
            for i in range(len(Buildings)):
                if i < 10: Labels[2+i] = Buildings[i+LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 2.2: #adding a building
            Labels[0] = 'What would you like to name this new Building?'
            AvailableButtons.append(3)

        elif PageNumber == 2.3: #deleting a building
            Labels[0] = 'Which Building would you like to remove from this list?'
            for i in range(len(Buildings)):
                if i < 10: Labels[2+i] = Buildings[i+LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 2.4: #asking which building to edit
            Labels[0] = 'Which Building would you like to edit?'
            for i in range(len(Buildings)):
                if i < 10: Labels[2+i] = Buildings[i+LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 2.5: #editing building name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].name)
            AvailableButtons.append(3)

        elif PageNumber == 3.0: #Viewing Rooms
            Labels[0] = ('Viewing ' + Buildings[Currents[0]].name + "'" + 's rooms')
            for i in range(len(Buildings[Currents[0]].rooms)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[i + LinePosition].name

            if len(Buildings[Currents[0]].rooms) <= 10:
                Labels[len(Buildings[Currents[0]].rooms) + 4] = 'What would you like to do?'
                Labels[len(Buildings[Currents[0]].rooms) + 5] = 'View Room'
                Labels[len(Buildings[Currents[0]].rooms) + 6] = 'Add Room'
                Labels[len(Buildings[Currents[0]].rooms) + 7] = 'Delete Room'
                Labels[len(Buildings[Currents[0]].rooms) + 8] = 'Edit Room'
                Labels[len(Buildings[Currents[0]].rooms) + 9] = 'Back'

            else:
                Labels[14] = 'What would you like to do?'
                Labels[15] = 'View Room'
                Labels[16] = 'Add Room'
                Labels[17] = 'Delete Room'
                Labels[18] = 'Edit Room'
                Labels[19] = 'Back'

            for i in range(5):
                if len(Buildings[Currents[0]].rooms) > 10: AvailableButtons.append(15 + i)
                else: AvailableButtons.append(len(Buildings[Currents[0]].rooms) + 5 + i)

        elif PageNumber == 3.1: #asking which room to view
            for i in range(len(Buildings[Currents[0]].rooms)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 3.2: #adding a room
            Labels[0] = 'What would you like to name this new Room?'
            AvailableButtons.append(3)

        elif PageNumber == 3.3: #deleting a room
            Labels[0] = 'Which Room would you like to remove from this list?'
            for i in range(len(Buildings[Currents[0]].rooms)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 3.4: #asking which room to edit
            Labels[0] = 'Which Room would you like to edit?'
            for i in range(len(Buildings[Currents[0]].rooms)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 3.5: #editing room name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].rooms[Currents[1]].name)
            AvailableButtons.append(3)

        elif PageNumber == 4.0: #Viewing items
            Labels[0] = ('Viewing ' + Buildings[Currents[0]].rooms[Currents[1]].name + "'" + 's items')

            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i + LinePosition].name
                if i < 10: labelColors[2+i] = 'Green'

            if len(Buildings[Currents[0]].rooms[Currents[1]].items) <= 10:
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 4] = 'What would you like to do?'
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 5] = 'View Item'
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 6] = 'Add Item'
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 7] = 'Delete Item'
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 8] = 'Edit Item'
                Labels[len(Buildings[Currents[0]].rooms[Currents[1]].items) + 9] = 'Back'
            else:
                Labels[14] = 'What would you like to do?'
                Labels[15] = 'View Item'
                Labels[16] = 'Add Item'
                Labels[17] = 'Delete Item'
                Labels[18] = 'Edit Item'
                Labels[19] = 'Back'

            for i in range(5):
                if len(Buildings[Currents[0]].rooms[Currents[1]].items) > 10: AvailableButtons.append(15 + i)
                else: AvailableButtons.append(len(Buildings[Currents[0]].rooms[Currents[1]].items) + 5 + i)

        elif PageNumber == 4.1: #asking which item to view
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 4.2: #adding a item
            Labels[0] = 'What would you like to name this new Item?'
            AvailableButtons.append(3)

        elif PageNumber == 4.3: #deleting a item
            Labels[0] = 'Which Item would you like to remove from this list?'
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 4.4: #asking which item to edit
            Labels[0] = 'Which Item would you like to edit?'
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 4.5: #editing item name
            Labels[0] = ('What would you like to rename ' + Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].name)
            AvailableButtons.append(3)

        elif PageNumber == 5.0: #viewing item
            Labels[0] = 'Viewing ' + Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].name + ' in ' + Buildings[Currents[0]].name + ' ' + Buildings[Currents[0]].rooms[Currents[1]].name
            Labels[2] = 'Amount: ' + str(Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].fullAmount)
            Labels[4] = 'Last Replaced: ' + Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].lastReplaced
            Labels[6] = 'Replaced Every ' + str(Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].replacementCycle)
            Labels[8] = 'Edit'
            Labels[9] = 'Back'

            AvailableButtons.append(8)
            AvailableButtons.append(9)

        elif PageNumber == 5.1: #Editing an item
            Labels[0] = 'What would you like to edit?'
            Labels[2] = 'Name'
            Labels[3] = 'Full Amount'
            Labels[4] = 'Replacement Time Frame'

            AvailableButtons.append(2)
            AvailableButtons.append(3)
            AvailableButtons.append(4)

        elif PageNumber == 6.0: #Viewing Delieveries
            Labels[0] = 'What would you like to do with Deliveries'
            Labels[2] = 'View Pending Orders'
            Labels[3] = 'Add a Delivery Order'
            Labels[4] = 'View Completed Deliveries'
            Labels[5] = 'Back'

            AvailableButtons.append(2)
            AvailableButtons.append(3)
            AvailableButtons.append(4)
            AvailableButtons.append(5)

        elif PageNumber == 6.1: #Viewing delivery list
            #for i in range(len(pendingDeliveries)):
            #    print(pendingDeliveries[i].location[0])
            Labels[0] = 'Viewing CMU Custodial Delivery List'

            for i in range(len(pendingDeliveries)):
                itemList = ''
                #for k in range(len(Deliveries)):
                #    itemList += (str(Deliveries[i+LinePosition].items[0][k].name) + ' ' + str(Deliveries[i+LinePosition].items[1][k].name) + ' ')
                if i < 9:
                    Labels[2+i] = (pendingDeliveries[i+LinePosition].location[0] + ' ' + pendingDeliveries[i+LinePosition].person) #+ ' ' + pendingDeliveries[i + LinePosition].location[1])
                    AvailableButtons.append(2+i)
                    if pendingDeliveries[i+LinePosition].staged: labelColors[2+i] = 'Blue'
                    else: labelColors[2+i] = 'Red'
                #if i < 10: Labels[2+i] = (str(Deliveries[i+LinePosition].number) + ' ' + Deliveries[i+LinePosition].location[0] + ' ' + itemList)

            if len(pendingDeliveries) <= 10:
                Labels[len(pendingDeliveries) + 4] = 'Back'
            else:
                Labels[14] = 'Back'

            if len(pendingDeliveries) >= 10: AvailableButtons.append(14)
            else: AvailableButtons.append(len(pendingDeliveries) + 4)

        elif PageNumber == 6.11: #Viewing a delivery
            Labels[0] = ('Viewing order #' + str(pendingDeliveries[Currents[3]].number) + ' in ' + pendingDeliveries[Currents[3]].location[0] + ' ' + pendingDeliveries[Currents[3]].location[1])

            for i in range(len(pendingDeliveries[Currents[3]].items)):
                if i < 10:
                    if str(pendingDeliveries[Currents[3]].items[i][0])[0] == '$':
                        Labels[2+i] = (inv.Inventory[str(pendingDeliveries[Currents[3]].items[i][0])] + ' -- ' + str(pendingDeliveries[Currents[3]].items[i][1][0]) + ' ' + str(pendingDeliveries[Currents[3]].items[i][1][1]))
                    else:
                        Labels[2+i] = (str(pendingDeliveries[Currents[3]].items[i][0]) + ' -- ' + str(pendingDeliveries[Currents[3]].items[i][1][0]) + ' ' + str(pendingDeliveries[Currents[3]].items[i][1][1]))

            Labels[2+len(pendingDeliveries[Currents[3]].items)] = Delivery.printTimeStamp(pendingDeliveries[Currents[3]].createDate)

            if len(pendingDeliveries[Currents[3]].items) <= 10:
                if pendingDeliveries[Currents[3]].staged: Labels[len(pendingDeliveries[Currents[3]].items) + 4] = 'Marks as Delivered'
                else: Labels[len(pendingDeliveries[Currents[3]].items) + 4] = 'Mark as Staged'
                Labels[len(pendingDeliveries[Currents[3]].items) + 5] = 'Back'
                AvailableButtons.append(len(pendingDeliveries[Currents[3]].items) + 4)
                AvailableButtons.append(len(pendingDeliveries[Currents[3]].items) + 5)
            else:
                if pendingDeliveries[Currents[3]].staged: Labels[14]= 'Mark as Delivered'
                else: Labels[14] = 'Mark as Staged'
                Labels[15] = 'Back'
                AvailableButtons.append(14)
                AvailableButtons.append(15)

        elif PageNumber == 6.2: #Adding a delivery // Checking Room
            Labels[0] = 'Which Building needs a delivery?'
            for i in range(len(Buildings)):
                if i < 10: Labels[2+i] = Buildings[i+LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 6.3: #Checking Room
            Labels[0] = 'Which room in ' + Buildings[Currents[0]].name + '?'
            for i in range(len(Buildings[Currents[0]].rooms)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[i+LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 6.4: #Adding Items
            Labels[0] = 'Which Items Would you like to add?'
            for i in range(len(Buildings[Currents[0]].rooms[Currents[1]].items)):
                if i < 10: Labels[2+i] = Buildings[Currents[0]].rooms[Currents[1]].items[i + LinePosition].name
                if i < 10: AvailableButtons.append(2+i)

        elif PageNumber == 6.5: #How many of that item?
            Labels[0] = 'How many ' + Buildings[Currents[0]].rooms[Currents[1]].items[Currents[2]].name + ' do you need?'
            AvailableButtons.append(3)

        elif PageNumber == 6.6: #Viewing completed deliveries list
            Labels[0] = 'Viewing Completed Deliveries'
            for i in range(len(completedDeliveries)):
                if i < 9:
                    Labels[2+i] = (completedDeliveries[i+LinePosition].location[0] + ' ' + completedDeliveries[i + LinePosition].location[1])
                    AvailableButtons.append(2+i)

            if len(completedDeliveries) <= 10:
                Labels[len(completedDeliveries)+2] = 'Back'
                AvailableButtons.append(len(completedDeliveries)+2)
            else:
                Labels[14] = 'Back'
                AvailableButtons.append(14)

        elif PageNumber == 6.7: #Viewing a completed delivery
            Labels[0] = 'Viewing ' + str(completedDeliveries[Currents[3]].person) + "'s order for " + str(completedDeliveries[Currents[3]].location[0])

            for i in range(len(completedDeliveries[Currents[3]].items)):
                if i < 10:
                    Labels[2+i] = (str(completedDeliveries[Currents[3]].items[i][1][0]) + ' '+ completedDeliveries[Currents[3]].items[i][1][1] + ' ' + str(completedDeliveries[Currents[3]].items[i][0]))

            if len(completedDeliveries[Currents[3]].items) <= 10:
                Labels[len(completedDeliveries[Currents[3]].items)+2] = 'Back'
                AvailableButtons.append(len(completedDeliveries[Currents[3]].items)+2)
            else:
                Labels[14] = 'Back'
                AvailableButtons.append(14)

        return Labels, AvailableButtons, labelColors
