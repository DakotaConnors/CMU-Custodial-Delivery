#Currently working on Version 0.2.0

import pygame
import PageManager as pm
import graphics as gr
import Location as loc
import Save
import datetime
import Inventory as inv
import Delivery
import ReadInventory

pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 25)

pageManager = pm.PageManager()

WIDTH = 1280
HEIGHT = 720
FPS = 30

currentBuilding = -1
currentRoom = -1
currentItem = -1
currentDelivery = -1

Shift = False
CurrentTime = (datetime.datetime.now())

Labels = []
labelNum = 0
labelColors = []

Buildings = []
pendingDeliveries = []
completedDeliveries = []
Inventory = ReadInventory.readInventory()
#for i in range(len(Inventory)):
#    print(Inventory[i].id, Inventory[i].name, Inventory[i].number)

orderingItems = []

#Deliveries.append(loc.Delivery('Trash Bag', 'Houston', (str(CurrentTime.month) + '/' + str(CurrentTime.day) + '/' + str(CurrentTime.year)), (str(CurrentTime.month) + '/' + str(CurrentTime.day + 2) + '/' + str(CurrentTime.year))))

saveTimer = 1000

#buttons
SubmitButton = gr.button((180,375), (80,30), pygame.image.load("Pictures\SubmitButton.png"))
LogInButton = gr.button((180,100), (80,30), pygame.image.load("Pictures\LogInButton.png"))
AtoZButton = gr.button((900,100), (80,30), pygame.image.load("Pictures\AtoZ.png"))
ZtoAButton = gr.button((985,100), (80,30), pygame.image.load("Pictures\ZtoA.png"))
BlankButtons = []
for i in range(10):
    BlankButtons.append(gr.button((0,0),(20,20),pygame.image.load("Pictures\Blank_Button.png")))
labelLocations = []#[(155, 0),(155, 15),(155, 30),(155, 45),(155, 60),(155, 75),(155, 90),(155, 105),(155, 120),(155, 135),(155, 150),(155, 165),(155, 180),(155, 195),(155, 210),(155, 225),(155, 240)]
labelNum = 0
for i in range(20):
    labelLocations.append((155,(5 + labelNum*30)))
    labelNum += 1
AvailableButtons = []

textBox = gr.textBox()
textBox.location = (175,labelLocations[3][1])
textBoxLabel = myfont.render(textBox.text, False, (0,0,0))
tempBox = ''

PageNumber = 0
LinePosition = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
rendered = False

def renderPage(Labels, labelColors):
    labelNum = 0
    for i in range(len(Labels)):
        if labelColors[i] == 'Green': tempLabel = myfont.render(Labels[i], False, (6,160,6))
        elif labelColors[i] == 'Blue': tempLabel = myfont.render(Labels[i], False, (6,160,240))
        elif labelColors[i] == 'Red': tempLabel = myfont.render(Labels[i], False, (222,0,0))
        else: tempLabel = myfont.render(Labels[i], False, (93,0,34))
        screen.blit(tempLabel, (180,(0 + labelNum)))
        labelNum += 30

    if PageNumber == 0.0:
        screen.blit(LogInButton.pic, (LogInButton.location[0], LogInButton.location[1]))
    elif PageNumber == 6.4: #Adding Submit Button
        screen.blit(SubmitButton.pic, (SubmitButton.location[0], SubmitButton.location[1]))
    elif PageNumber == 2.0:
        screen.blit(AtoZButton.pic,(AtoZButton.location[0], AtoZButton.location[1]))
        screen.blit(ZtoAButton.pic,(ZtoAButton.location[0], ZtoAButton.location[1]))

    #elif (PageNumber == 1.0 or PageNumber == 2.0 or PageNumber == 2.2):
    for i in range(len(AvailableButtons)):
        #print(PageNumber, str(len(BlankButtons)), str(len(AvailableButtons)), str(len(labelLocations)))
        BlankButtons[i].location = (labelLocations[AvailableButtons[i]][0], labelLocations[AvailableButtons[i]][1])
        screen.blit(BlankButtons[i].pic, (labelLocations[AvailableButtons[i]][0], labelLocations[AvailableButtons[i]][1]))

    #timeLabel = myfont.render((str(CurrentTime.month) + '/' + str(CurrentTime.day) + '/' + str(CurrentTime.year)), False, (0,0,0))
    timeLabel = myfont.render(str(PageNumber), False, (0,0,0))
    screen.blit(timeLabel, (0,690))

def checkOrders():
    ordersToAdd = Save.loadOrders()
    if ordersToAdd != '':
        stringTokens = ordersToAdd.split(' ')
        #print(stringTokens)
        tempPerson = stringTokens[0]
        tempLocation = (stringTokens[1], 'Closet')
        tempComplete = stringTokens[2]
        tempCreate = '(date created)'

        tempItems = []
        for i in range(3,len(stringTokens)-2,3):
            tempItems.append((stringTokens[i], (stringTokens[i+1], stringTokens[i+2])))

        pendingDeliveries.append(Delivery.Delivery(tempPerson, tempItems, tempLocation, tempCreate, tempComplete))


        '''
        tempItems = orderingItems
        tempLocation = (Buildings[currentBuilding].name, Buildings[currentBuilding].rooms[currentRoom].name)
        tempCreate = 'date'
        tempComplete = 'date + 2'

        pendingDeliveries.append(loc.Delivery(tempItems, tempLocation, tempCreate, tempComplete))

        orderingItems.append((loc.Item(Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name), textBox.text))
        '''


        #create a new pending delivery based off this information

Buildings = Save.loadBuildings()
completedDeliveries = Save.loadCompletedOrders()
pendingDeliveries = Save.loadPendingOrders()

while not(done):
    checkOrders()
    if not(rendered):
        Labels, AvailableButtons, labelColors = pageManager.ChangePage(PageNumber, Buildings, (currentBuilding, currentRoom, currentItem, currentDelivery), LinePosition, pendingDeliveries, completedDeliveries)
        #print('rendering page', PageNumber)
        screen.blit(pygame.image.load("Pictures\Main_Background.png"), (0,0))
        if (textBox.inUse): screen.blit(textBoxLabel, textBox.location)
        renderPage(Labels, labelColors)
        rendered = True

        #saving things
        Save.savePendingOrders(pendingDeliveries)
        Save.saveCompletedOrders(completedDeliveries)
        Save.saveBuildings(Buildings)

    '''
    if saveTimer > 0:
        saveTimer -= 1
        if saveTimer % 100 == 0: Save.save(Buildings, pendingDeliveries, completedDeliveries)
    else:
        saveTimer = 1000
        Save.SaveCurrentOrders(pendingDeliveries)
    '''

    #Checking delivery dates

    #checking TextBox cursor
    if textBox.inUse:
        if textBox.timer == 0: rendered = False
        textBox.checkTimer()
        if textBox.visible:
            text_width, text_height = myfont.size(textBox.text)
            screen.blit(textBox.cursor, (textBox.location[0] + text_width, textBox.location[1] + 6))
            rendered = False
        if tempBox != textBox.text:
            textBoxLabel = myfont.render(textBox.text, False, (0,0,0))
            screen.blit(textBoxLabel, textBox.location)
            tempBox = textBox.text

    #checking for buttons clicks
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:

        if PageNumber == 0.0:
            if LogInButton.checkCollision(event.pos):
                PageNumber = 1.0
                rendered = False

        elif PageNumber == 1.0:
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #viewing buildings list
                        PageNumber = 2.0
                        rendered = False
                    elif i == 1: #viewing delieveries
                        PageNumber = 6.0
                        rendered = False
                    elif i == 2:
                        PageNumber = 0
                        rendered = False

        elif PageNumber == 2.0: #Viewing Building List
            if AtoZButton.checkCollision(event.pos):
                Buildings = pageManager.sortBuildingsAtoZ(Buildings)
                rendered = False
            elif ZtoAButton.checkCollision(event.pos):
                Buildings = pageManager.sortBuildingsZtoA(Buildings)
                rendered = False
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #view a building
                        PageNumber = 2.1
                        LinePosition = 0
                        rendered = False
                    elif i == 1: #Add a building
                        PageNumber = 2.2
                        LinePosition = 0
                        rendered = False
                        textBox.inUse = True
                    elif i == 2: #Deleting a building
                        PageNumber = 2.3
                        LinePosition = 0
                        rendered = False
                    elif i == 3: #editing a building
                        PageNumber = 2.4
                        LinePosition = 0
                        rendered = False
                    elif i == 4: #back
                        PageNumber = 1.0
                        LinePosition = 0
                        rendered = False

        elif PageNumber == 2.1: #Asking which building to view
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentBuilding = i + LinePosition
                    PageNumber = 3.0
                    rendered = False
                    LinePosition = 0

        elif PageNumber == 2.2: #Adding a buildings
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 2.0
                        rendered = False

                        Buildings.append(loc.Building(textBox.text))
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 2.3: #Deleting a building
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    del Buildings[i + LinePosition]
                    LinePosition = 0
                    PageNumber = 2.0
                    rendered = False

        elif PageNumber == 2.4: #asking which building to edit
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentBuilding = i + LinePosition
                    PageNumber = 2.5
                    rendered = False
                    textBox.inUse = True

        elif PageNumber == 2.5: #editing building
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 2.0
                        rendered = False
                        Buildings[currentBuilding].name = textBox.text
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 3.0: #viewing current building
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #view a room
                        PageNumber = 3.1
                        rendered = False
                    elif i == 1: #Add a room
                        PageNumber = 3.2
                        rendered = False
                        textBox.inUse = True
                    elif i == 2: #Deleting a room
                        PageNumber = 3.3
                        rendered = False
                    elif i == 3: #editing a room
                        PageNumber = 3.4
                        rendered = False
                    elif i == 4: #back
                        PageNumber = 2.0
                        rendered = False

        elif PageNumber == 3.1: #view a room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentRoom = i + LinePosition
                    PageNumber = 4.0
                    rendered = False

        elif PageNumber == 3.2: #Adding a new room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 3.0
                        rendered = False

                        Buildings[currentBuilding].rooms.append(loc.Room(textBox.text))
                        for key in inv.Inventory:
                            #print (key, 'corresponds to', inv.Inventory[key])
                            Buildings[currentBuilding].rooms[len(Buildings[currentBuilding].rooms)-1].items.append(loc.Item(inv.Inventory[key]))
                        #for i in range(len(inv.Inventory)):
                        #    Buildings[currentBuilding].rooms[len(Buildings[currentBuilding].rooms) - 1].items.append(loc.Item(inv.Inventory[1]))
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 3.3: #deleting a room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    del Buildings[currentBuilding].rooms[i + LinePosition]
                    LinePosition = 0
                    PageNumber = 3.0
                    rendered = False

        elif PageNumber == 3.4: #asking which room to edit
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentRoom = i + LinePosition
                    PageNumber = 3.5
                    rendered = False
                    textBox.inUse = True

        elif PageNumber == 3.5: #editing room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 3.0
                        rendered = False
                        Buildings[currentBuilding].rooms[currentRoom].name = textBox.text
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 4.0: #viewing current item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #view an item
                        PageNumber = 4.1
                        LinePosition = 0
                        rendered = False
                    elif i == 1: #Add an item
                        PageNumber = 4.2
                        LinePosition = 0
                        rendered = False
                        textBox.inUse = True
                    elif i == 2: #Deleting an item
                        PageNumber = 4.3
                        LinePosition = 0
                        rendered = False
                    elif i == 3: #editing an item
                        PageNumber = 4.4
                        LinePosition = 0
                        rendered = False
                    elif i == 4: #back
                        PageNumber = 3.0
                        LinePosition = 0
                        rendered = False

        elif PageNumber == 4.1: #view an item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentItem = i
                    PageNumber = 5.0
                    rendered = False

        elif PageNumber == 4.2: #Adding a new item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 4.0
                        rendered = False

                        Buildings[currentBuilding].rooms[currentRoom].items.append(loc.Item(textBox.text))
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 4.3: #deleting an item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    del Buildings[currentBuilding].rooms[currentItem].items[i]
                    LinePosition = 0
                    PageNumber = 4.0
                    rendered = False

        elif PageNumber == 4.4: #asking which item to edit
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentItem = i
                    PageNumber = 4.5
                    rendered = False
                    textBox.inUse = True

        elif PageNumber == 4.5: #editing item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 4.0
                        rendered = False
                        Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name = textBox.text
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 5.0: #viewing an item
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0:
                        PageNumber = 5.1
                        rendered = False
                    elif i == 1:
                        PageNumber = 4.0
                        rendered = False

        elif PageNumber == 6.0: #Viewing Delievries Main Page
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0:
                        PageNumber = 6.1 #Viewing List of delieveries
                        LinePosition = 0
                        rendered = False
                    if i == 1:
                        PageNumber = 6.2 #Add a delivery
                        LinePosition = 0
                        rendered = False
                    if i == 2: #View list of completed Deliveries
                        PageNumber = 6.6
                        LinePosition = 0
                        rendered = False
                    if i == 3: #Back
                        PageNumber = 1
                        LinePosition = 0
                        rendered = False

        elif PageNumber == 6.1: #View pending Deliveries List
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == len(AvailableButtons) - 1: #Back
                        PageNumber = 6.0 #Back
                        rendered = False
                    else:
                        currentDelivery = i + LinePosition
                        PageNumber = 6.11
                        rendered = False

        elif PageNumber == 6.11: #Viewing all items in a delivery
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #Staging/Delivering a delivery
                        if not(pendingDeliveries[currentDelivery].staged): pendingDeliveries[currentDelivery].staged = True
                        else:
                            completedDeliveries.append(pendingDeliveries[currentDelivery])
                            Save.saveCompletedOrders(completedDeliveries)

                            LinePosition = 0

                            Save.deletePendingOrder(pendingDeliveries[currentDelivery].number)
                            del pendingDeliveries[currentDelivery]

                        PageNumber = 6.1
                        rendered = False

                    elif i == 1: #back
                        PageNumber = 6.1
                        rendered = False

        elif PageNumber == 6.2: #Asking which building for Delivery
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentBuilding = i + LinePosition
                    PageNumber = 6.3
                    rendered = False
                    LinePosition = 0

        elif PageNumber == 6.3: #Checking off a list of items
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentRoom = i + LinePosition
                    PageNumber = 6.4
                    rendered = False
                    LinePosition = 0

        elif PageNumber == 6.4: #checking which item

            if SubmitButton.checkCollision(event.pos): #submit
                PageNumber = 6.0
                rendered = False
                LinePosition = 0

                tempItems = orderingItems
                tempLocation = (Buildings[currentBuilding].name, Buildings[currentBuilding].rooms[currentRoom].name)
                now = datetime.datetime.now()
                tempCreate = Delivery.getTimeStamp(now.month, now.day, now.year, now.hour, now.minute, now.second)
                tempNumber = "ADMIN_" + Buildings[currentBuilding].name + "_" + tempCreate
                tempComplete = 'NOT COMPLETE'

                pendingDeliveries.append(Delivery.Delivery("Admin", tempNumber, tempItems, tempLocation, tempCreate, tempComplete))
                orderingItems = []

            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentItem = i + LinePosition
                    PageNumber = 6.5
                    rendered = False
                    LinePosition = 0
                    textBox.inUse = True
                    textBox.text = ''


        elif PageNumber == 6.5: #add item to list
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        #tempItems.append((stringTokens[i], (stringTokens[i+1], stringTokens[i+2])))
                        stringTokens = textBox.text.split(' ')
                        if stringTokens == ['']: orderingItems.append((Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name, ('1', 'Case')))
                        elif len(stringTokens) < 2: orderingItems.append((Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name, (stringTokens[0], 'Case')))
                        else: orderingItems.append((Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name, (stringTokens[0], stringTokens[1])))
                        #orderingItems.append((loc.Item(Buildings[currentBuilding].rooms[currentRoom].items[currentItem].name), textBox.text))
                        PageNumber = 6.4
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 6.6: #Viewing completed Orders List
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == (len(AvailableButtons) - 1): #back
                        PageNumber = 6.0
                        rendered = False
                    else:
                        currentDelivery = i + LinePosition
                        PageNumber = 6.7
                        rendered = False

        elif PageNumber == 6.7: #viewing a completed order
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == (len(AvailableButtons) - 1): #back
                        PageNumber = 6.6
                        rendered = False

    elif event.type == pygame.QUIT:
        done = True

    elif event.type == pygame.KEYDOWN:
        key = textBox.whichKey(event.key)
        if key == 'BACKSPACE': textBox.text = textBox.text[:-1]
        elif key == 'SHIFT':
            if Shift: Shift = False
            else: Shift = True
        elif key == 'SAVE':
            Save.save(Buildings, pendingDeliveries, completedDeliveries)
        elif key == 'LOAD':
            Buildings, pendingDeliveries, completedDeliveries = Save.load()
        elif key == 'UP':
            if LinePosition > 0: LinePosition -= 1
            rendered = False
        elif key == 'DOWN':
            if ((PageNumber >= 2.0 and PageNumber < 3.0) or PageNumber == 6.2):
                if len(Buildings) - LinePosition > 10:
                    LinePosition += 1
                    rendered = False
            elif PageNumber >= 3.0 and PageNumber < 4.0:
                if len(Buildings[currentBuilding].rooms) - LinePosition > 10:
                    LinePosition += 1
                    rendered = False
            elif ((PageNumber >= 4.0 and PageNumber < 5.0) or PageNumber == 6.4):
                if len(Buildings[currentBuilding].rooms[currentRoom].items) - LinePosition > 10:
                    LinePosition += 1
                    rendered = False

            elif PageNumber >= 6.0 and PageNumber < 6.6:
                if len(pendingDeliveries) - LinePosition > 9:
                    LinePosition += 1
                    rendered = False

            elif PageNumber >= 6.6 and PageNumber < 7.0:
                if len(completedDeliveries) - LinePosition > 9:
                    LinePosition += 1
                    rendered = False

        else:
            if Shift:
                textBox.text += key.upper()
                Shift = False
            else: textBox.text += key
    pygame.display.flip()
