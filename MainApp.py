import pygame
import PageManager as pm
import graphics as gr
import Location as loc
import Save

pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman', 25)

pageManager = pm.PageManager()

WIDTH = 1280
HEIGHT = 720
FPS = 30

currentBuilding = -1
currentRoom = -1
currentItem = -1

Shift = False

Labels = []
labelNum = 0
Buildings = []

saveTimer = 10000

#buttons
LogInButton = gr.button((180,100), (80,30), pygame.image.load("Pictures\LogInButton.png"))
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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
rendered = False

def renderPage(Labels):
    labelNum = 0
    for i in range(len(Labels)):
        tempLabel = myfont.render(Labels[i], False, (93,0,34))
        screen.blit(tempLabel, (180,(0 + labelNum)))
        labelNum += 30

    if PageNumber == 0.0:
        screen.blit(LogInButton.pic, (LogInButton.location[0], LogInButton.location[1]))

    #elif (PageNumber == 1.0 or PageNumber == 2.0 or PageNumber == 2.2):
    for i in range(len(AvailableButtons)):
        BlankButtons[i].location = (labelLocations[AvailableButtons[i]][0], labelLocations[AvailableButtons[i]][1])
        screen.blit(BlankButtons[i].pic, (labelLocations[AvailableButtons[i]][0], labelLocations[AvailableButtons[i]][1]))

Buildings = Save.load()
while not(done):
    if not(rendered):
        Labels, AvailableButtons = pageManager.ChangePage(PageNumber, Buildings, (currentBuilding, currentRoom, currentItem))
        #print('rendering page', PageNumber)
        screen.blit(pygame.image.load("Pictures\Main_Background.png"), (0,0))
        if (textBox.inUse): screen.blit(textBoxLabel, textBox.location)
        renderPage(Labels)
        rendered = True

    if saveTimer > 0: saveTimer -= 1
    else:
        saveTimer = 10000
        Save.save(Buildings)

    #checking TextBox cursor
    if textBox.inUse:
        if textBox.timer == 0: rendered = False
        textBox.checkTimer()
        if textBox.visible:
            text_width, text_height = myfont.size(textBox.text)
            screen.blit(textBox.cursor, (textBox.location[0] + text_width, textBox.location[1] - 10))
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
                    if i == 0:
                        PageNumber = 2.0
                        rendered = False
                    elif i == 1:
                        print('Back Button Clicked')
                        PageNumber = 0
                        rendered = False

        elif PageNumber == 2.0: #Viewing Building List
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #view a building
                        PageNumber = 2.1
                        rendered = False
                    elif i == 1: #Add a building
                        PageNumber = 2.2
                        rendered = False
                        textBox.inUse = True
                    elif i == 2: #Deleting a building
                        PageNumber = 2.3
                        rendered = False
                    elif i == 3: #editing a building
                        PageNumber = 2.4
                        rendered = False
                    elif i == 4: #back
                        PageNumber = 1.0
                        rendered = False

        elif PageNumber == 2.1: #Asking which building to view
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentBuilding = i
                    PageNumber = 3.0
                    rendered = False

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
                    del Buildings[i]
                    PageNumber = 2.0
                    rendered = False

        elif PageNumber == 2.4: #asking which building to edit
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentBuilding = i
                    PageNumber = 2.5
                    rendered = False
                    textBox.inUse = True

        elif PageNumber == 2.5: #editing building
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 2.0
                        rendered = False
                        Buildings[i].name = textBox.text
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
                    currentRoom = i
                    PageNumber = 4.0
                    rendered = False

        elif PageNumber == 3.2: #Adding a new room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    if i == 0: #enter
                        PageNumber = 3.0
                        rendered = False

                        Buildings[currentBuilding].rooms.append(loc.Room(textBox.text))
                        textBox.text = ''
                        textBox.inUse = False

        elif PageNumber == 3.3: #deleting a room
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    del Buildings[currentBuilding].rooms[i]
                    PageNumber = 3.0
                    rendered = False

        elif PageNumber == 3.4: #asking which room to edit
            for i in range(len(AvailableButtons)):
                if BlankButtons[i].checkCollision(event.pos):
                    currentRoom = i
                    PageNumber = 3.5
                    rendered = False
                    textBox.inUse = True

        elif PageNumber == 3.5: #editing building
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
                        rendered = False
                    elif i == 1: #Add an item
                        PageNumber = 4.2
                        rendered = False
                        textBox.inUse = True
                    elif i == 2: #Deleting an item
                        PageNumber = 4.3
                        rendered = False
                    elif i == 3: #editing an item
                        PageNumber = 4.4
                        rendered = False
                    elif i == 4: #back
                        PageNumber = 3.0
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

    elif event.type == pygame.QUIT:
        done = True

    elif event.type == pygame.KEYDOWN:
        key = textBox.whichKey(event.key)
        if key == 'BACKSPACE': textBox.text = textBox.text[:-1]
        elif key == 'SHIFT':
            if Shift: Shift = False
            else: Shift = True
        elif key == 'SAVE':
            Save.save(Buildings)
        elif key == 'LOAD':
            Buildings = Save.load()
        else:
            if Shift:
                textBox.text += key.upper()
                Shift = False
            else: textBox.text += key
    pygame.display.flip()
