import time
import datetime
import pickle
import Delivery
import glob
import os


def save(Buildings, pendingDeliveries, completedDeliveries):
    output_file = open("tempSave.bin", "wb")
    #print('saving')
    pickle.dump(Buildings, output_file)
    pickle.dump(pendingDeliveries, output_file)
    pickle.dump(completedDeliveries, output_file)
    output_file.close()

def savePendingOrders(pendingDeliveries):
    for delivery in pendingDeliveries:
        fileString = 'saves/pendingOrders/'
        fileString += delivery.number + '.bin'
        output_file = open(fileString, "wb")
        pickle.dump(delivery, output_file)
        output_file.close()

def saveCompletedOrders(completedDeliveries):
    for delivery in completedDeliveries:
        fileString = 'saves/completedOrders/'
        fileString += delivery.number + '.bin'
        output_file = open(fileString, "wb")
        pickle.dump(delivery, output_file)
        output_file.close()

def saveBuildings(Buildings):
    fileString = "saves/Buildings"
    output_file = open(fileString + ".bin", "wb")
    pickle.dump(Buildings, output_file)
    output_file.close()

def loadPendingOrders():
    fileList = glob.glob("saves/pendingOrders/*.bin")
    fixedFileList = []
    pendingDeliveries = []
    for fileName in fileList:
        #print(fileName[20:])
        fixedFileList.append(fileName)

    for file in fixedFileList:
        input_file = open(file, "rb")
        try:
            pendingDeliveries.append(pickle.load(input_file))
        except (EOFError):
            pendingDeliveries.append("SOMETHING WENT WRONG")

    return pendingDeliveries

def loadCompletedOrders():
    fileList = glob.glob("saves/completedOrders/*.bin")
    fixedFileList = []
    completedDeliveries = []
    for fileName in fileList:
        #print(fileName[20:])
        fixedFileList.append(fileName)

    for file in fixedFileList:
        input_file = open(file, "rb")
        try:
            completedDeliveries.append(pickle.load(input_file))
        except (EOFError):
            completedDeliveries.append("SOMETHING WENT WRONG")

    return completedDeliveries

def loadBuildings():
    fileString = "saves/Buildings.bin"
    Buildings = []
    input_file = open(fileString, "rb")
    try:
        Buildings = pickle.load(input_file)
    except (EOFError):
        print("SOMETHING WENT WRONG LOADING BUILDINGS")

    return Buildings

def deletePendingOrder(fileName):
    os.remove('C:/Users/Dakota/Documents/School/Software_Engineering/Delivery_App/saves/pendingOrders/' + fileName + '.bin')

def load():
    input_file = open("tempSave.bin", "rb")
    #print('loading')
    try:
        Buildings = pickle.load(input_file)
    except (EOFError):
        Buildings = []

    try:
        pendingDeliveries = pickle.load(input_file)
    except (EOFError):
        pendingDeliveries = []

    try:
        completedDeliveries = pickle.load(input_file)
    except (EOFError):
        completedDeliveries = []

    input_file.close()
    return Buildings

def loadOrders():
    input_file = open("orders.bin", "rb")
    try:
        order = pickle.load(input_file)
    except (EOFError):
        order = "NO ORDER"
    output_file = open("orders.bin", "wb")
    pickle.dump("", output_file)
    output_file.close()
    return order

def SaveCurrentOrders(pendingDeliveries):
    output_file = open("currentOrders.bin", "wb")
    for delivery in pendingDeliveries:
        now = datetime.datetime.now()
        #print("saving delivery for: " + delivery.location[0] + str(now.year))
    pickle.dump(pendingDeliveries, output_file)
    output_file.close()
