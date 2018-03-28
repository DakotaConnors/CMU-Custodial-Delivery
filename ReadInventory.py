import csv
import Location as loc
inventory = []

def readInventory():
    with open('Inventory.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i = 1
        for row in readCSV:
            inventory.append(loc.InventoryItem(row[0], row[1], row[2]))
            #print(row[0],row[1],row[2])
            i += 1

    return inventory
