import Location as loc
from User import User
import os
import pygame
#import TextBox

clear = lambda: os.system('cls')
done = False
loggedIn = False
Page = 0.0
buildings = []
currentBuilding = 0
currentRoom = 0
currentItem = 0



while(not(done)):
    #print(Page)
    if not(loggedIn):
        print('Please enter a username')
        username = input()
        user = User(username, 'password')
        loggedIn = True
        clear()

    elif Page == 0.0:
        print('What would you like to do? (enter a number)\n(1) View Buildings\n(2) Exit')
        option = input()
        if option == '1':
            Page = 1.0
            clear()
        elif option == '2':
            done = True

    elif Page == 1.0: #viewing buildings
        for i in range(len(buildings)):
            print('('+ str(i+1) + ')',buildings[i].name)
        print('\nWhat would you like to do? (enter a number)\n(1) Add Builing\n(2) View Building\n(3) Delete Building\n(4) Edit Building\n(5) Back\n')
        option = input()
        if option == '1':
            Page = 1.1
        elif option == '2':
            Page = 1.2
        elif option == '3':
            Page = 1.3
        elif option == '4':
            Page = 1.4
        elif option == '5':
            Page = 0
        clear()

    elif Page == 1.1: #Adding a building
        print('What would you like to name this Building?')
        name = input()
        buildings.append(loc.Building(name))
        Page = 1.0
        clear()

    elif Page == 1.2: #Asking what building to view
        print('Which building would you like to view? (enter a number)')
        for i in range(len(buildings)):
            print('('+ str(i+1) + ')', buildings[i].name)
        intOption = int(input())
        for i in range(len(buildings)):
            if ((i+1) == intOption):
                currentBuilding = i
                Page = 2.0
        clear()

    elif Page == 1.3: #Deleting a building
        print('Which building would you like to delete? (enter a number)')
        for i in range(len(buildings)):
            print('('+ str(i+1) + ')', buildings[i].name)
        intOption = int(input())
        for i in range(len(buildings)):
            if ((i+1) == intOption):
                del buildings[i]
                Page = 1.0
        clear()

    elif Page == 1.4: #Choosing a building to edit
        print('Which building would you like to edit? (enter a number)')
        for i in range(len(buildings)):
            print('('+ str(i+1) + ')', buildings[i].name)
        intOption = int(input())
        for i in range(len(buildings)):
            if ((i+1) == intOption):
                Page = 1.5
                currentBuilding = i
        clear()

    elif Page == 1.5: #Editing a building
        print('What would you like to rename this building?')
        tempName = input()
        buildings[i].setName(tempName)

    elif Page == 2.0: #Viewing Rooms
        for i in range(len(buildings[currentBuilding].rooms)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[i].name)
        print('What would you like to do? (enter a number)\n(1) Add Room\n(2) View Room\n(3) Delete Room\n(4) Edit Room\n(5) Back')
        option = input()
        if option == '1':
            Page = 2.1
        elif option == '2':
            Page = 2.2
        elif option == '3':
            Page = 2.3
        elif option == '4':
            Page = 2.4
        elif option == '5':
            Page = 1
        clear()

    elif Page == 2.1: #Adding a room
        print('What would you like to name this new Room?')
        tempName = input()
        buildings[currentBuilding].rooms.append(loc.Room(tempName))
        Page = 2.0
        clear()

    elif Page == 2.2: #Asking which room to view
        for i in range(len(buildings[currentBuilding].rooms)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[i].name)
        print('Which room would you like to view? (enter a number)')
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms)):
            if ((i+1) == intOption):
                currentRoom = i
                Page = 3.0
        clear()

    elif Page == 2.3: #Asking which room to Delete
        for i in range(len(buildings[currentBuilding].rooms)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[i].name)
        print('Which room would you like to delete? (enter a number)')
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms)):
            if ((i+1) == intOption):
                del buildings[currentBuilding].rooms[i]
                Page = 2.0
        clear()

    elif Page == 2.4: #Choosing a room to edit
        print('Which room would you like to edit? (enter a number)')
        for i in range(len(buildings[currentBuilding].rooms)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[i].name)
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms)):
            if ((i+1) == intOption):
                Page = 2.5
                currentRoom = i
        clear()

    elif Page == 2.5: #Editing a room
        print('What would you like to rename this room?')
        tempName = input()
        buildings[currentBuilding].rooms[currentRoom].setName(tempName)
        Page = 2.0
        clear()

    elif Page == 3.0:
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[currentRoom].items[i].name)
        print('What would you like to do? (enter a number)\n(1) Add Item\n(2) View Item\n(3) Delete Item\n(4) Edit Item\n(5) Back')
        option = input()
        if option == '1':
            Page = 3.1
        elif option == '2':
            Page = 3.2
        elif option == '3':
            Page = 3.3
        elif option == '4':
            Page = 3.4
        elif option == '5':
            Page = 2
        clear()

    elif Page == 3.1: #Adding an item
        print('What would you like to name this new Item?')
        tempName = input()
        buildings[currentBuilding].rooms[currentRoom].items.append(loc.Item(tempName))
        Page = 3.0
        clear()

    elif Page == 3.2: #Asking which item to view
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[currentRoom].items[i].name)
        print('Which room would you like to view? (enter a number)')
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            if ((i+1) == intOption):
                currentItem = i
                Page = 4.0
        clear()

    elif Page == 3.3: #Asking which item to Delete
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            print('('+ str(i+1) + ')', buildings[currentBuilding].rooms[currentRoom].items[i].name)
        print('Which item would you like to delete? (enter a number)')
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            if ((i+1) == intOption):
                del buildings[currentBuilding].rooms[currentRoom].items[i]
                Page = 3.0
        clear()

    elif Page == 3.4: #Choosing a item to edit
        print('Which item would you like to edit? (enter a number)')
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            print(i+1, buildings[currentBuilding].rooms[i].name)
        intOption = int(input())
        for i in range(len(buildings[currentBuilding].rooms[currentRoom].items)):
            if ((i+1) == intOption):
                Page = 3.5
                currentItem = i
        clear()

    elif Page == 3.5: #Editing a room
        print('What would you like to rename this Item?')
        tempName = input()
        buildings[currentBuilding].rooms[currentRoom].items[currentItem].setName(tempName)
        Page = 3.0
        clear()

    elif Page == 4.0: #viewing items
        print('What would you like to do?')
        option = input()
        if option == '1':
            Page = 3.0
        clear()

print('Goodbye')
