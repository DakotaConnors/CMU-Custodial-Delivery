#http://flask.pocoo.org/docs/0.12/quickstart/

#https://www.youtube.com/watch?v=lUCmVNGs5gw&t=274s
#https://www.youtube.com/watch?v=ZVGwqnjOKjk




from flask import Flask, request, render_template, redirect, url_for
import webAppSave
import Save
import ReadInventory
import numpy as np
import Location
import Delivery
import datetime

app = Flask(__name__)

Inventory = ReadInventory.readInventory()
ids = []
names = []
numbers = []
for item in Inventory:
    #print(item.id,item.name,item.number)
    ids.append(item.id)
    names.append(item.name)
    numbers.append(item.number)

length = len(Inventory)
building = ""
person = ""
category = ""
orderItems = []
orderAmounts = []

currentOrders = []
currentOrder = None


@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('home'))

@app.route('/home/', methods=['POST', 'GET'])
def home():
    global orderItems, orderAmounts
    orderItems = []
    orderAmounts = []

    if request.method == 'POST':
        choice = request.form['option']
        if choice == 'orders': return redirect(url_for('ordering'))
        elif choice == 'deliveries': return redirect(url_for('deliveries'))
        elif choice == 'interactiveOrderForm': return redirect(url_for('interactiveOrderForm'))

    return render_template('index.html')

@app.route('/ordering/', methods=['POST', 'GET'])
def ordering():
    if request.method == 'POST':
        User = request.form['person']
        Building = request.form['building']
        Item1 = request.form['item1']
        Quantity1 = request.form['quantity1']
        Item2 = request.form['item2']
        Quantity2 = request.form['quantity2']
        Item3 = request.form['item3']
        Quantity3 = request.form['quantity3']
        Item4 = request.form['item4']
        Quantity4 = request.form['quantity4']
        Item5 = request.form['item5']
        Quantity5 = request.form['quantity5']

        now = datetime.datetime.now()
        order = User + ' ' + Building + ' ' + Delivery.getTimeStamp(now.month, now.day, now.year, now.hour, now.minute, now.second) + ' '
        if Item1 != 'Nothing' : order += ' $' + Item1 + ' ' + Quantity1
        if Item2 != 'Nothing' : order += ' $' + Item2 + ' ' + Quantity2
        if Item3 != 'Nothing' : order += ' $' + Item3 + ' ' + Quantity3
        if Item4 != 'Nothing' : order += ' $' + Item4 + ' ' + Quantity4
        if Item5 != 'Nothing' : order += ' $' + Item5 + ' ' + Quantity5
        print(order)
        webAppSave.save(order)
        return redirect(url_for('finishedOrder'))

    return render_template('orderForm.html')

@app.route('/submitted/', methods=['POST', 'GET'])
def finishedOrder():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('submit.html')

@app.route('/deliveries/', methods=['POST', 'GET'])
def deliveries():
    if request.method == 'POST':
        if request.form['click'] == 'Search':
            option = request.form['order']
            global currentOrders, currentOrder
            for order in currentOrders:
                tempTokens = option.split('/')
                tempString = tempTokens[0] + '-' + tempTokens[1] + '-' + tempTokens[2]
                tempTokens = tempString.split(':')
                tempString = tempTokens[0] + '-' + tempTokens[1] + '-' + tempTokens[2] + '-'
                tempTokens = tempString.split(' ')
                tempString = tempTokens[0] + '-' + tempTokens[1]
                if (order.number == tempString):
                    currentOrder = order
            return redirect(url_for('viewDelivery'))
        if request.form['click'] == 'Home':
            return redirect(url_for('home'))

    currentOrders = Save.loadPendingOrders()
    names = []
    buildings = []
    numbers = []

    for order in currentOrders:
        tempString = order.number.split('_')
        names.append(tempString[0])
        buildings.append(tempString[1])
        numbers.append(Delivery.printTimeStamp(tempString[2]))

    return render_template('deliveries.html', names=names, buildings=buildings, numbers=numbers)

@app.route('/deliveries/viewDelivery/', methods=['POST', 'GET'])
def viewDelivery():
    if request.method == 'POST':
        if request.form['click'] == 'Mark as Staged':
            currentOrder.staged = True
            for order in currentOrders:
                if order.number == currentOrder.number:
                    order = currentOrder
            Save.savePendingOrders(currentOrders)
            return redirect(url_for('deliveries'))
        if request.form['click'] == "Mark as Delivered":
            for order in currentOrders:
                if order.number == currentOrder.number:
                    tempList = []
                    tempList.append(order)
                    Save.saveCompletedOrders(tempList)
                    Save.deletePendingOrder(order.number)
                    currentOrders.remove(order)
            return redirect(url_for('deliveries'))
        if request.form['click'] == "Home":
            return redirect(url_for('home'))


    currentPerson = currentOrder.person
    currentBuilding = currentOrder.location[0]
    currentItems = []
    currentAmounts = []
    for item in currentOrder.items:
        currentItems.append(item[0])
        currentAmounts.append(item[1])

    staged = currentOrder.staged
    return render_template('viewDelivery.html', currentPerson=currentPerson, currentBuilding=currentBuilding, currentItems=currentItems, currentAmounts=currentAmounts, staged=staged)

@app.route('/interactiveOrderForm/', methods=['POST', 'GET'])
def interactiveOrderForm():
    if request.method == 'POST':
        if request.form['click'] == 'Next':
            global building, person
            building = request.form['building']
            person = request.form['person']
            return redirect(url_for('interactiveOrderFormCategory'))
        elif request.form['click'] == 'Home':
            return redirect(url_for('home'))
    return render_template('interactiveOrderForm.html')

@app.route('/interactiveOrderForm/chooseCategory', methods=['POST','GET'])
def interactiveOrderFormCategory():
    if request.method == 'POST':
        if request.form['click'] == 'Search':
            global category
            category = request.form['category']
            return redirect(url_for('interactiveOrderFormItem'))
        elif request.form['click'] == 'Home':
            return redirect(url_for('home'))
        elif request.form['click'] == 'Submit Order':
            #global orderItems, orderAmounts
            #orderItems.append(request.form['item'])
            #orderAmounts.append((request.form['number'] + " " + request.form['type']))
            return redirect(url_for('interactiveOrderFormConfirm'))
    return render_template('interactiveOrderFormChooseCategory.html', building=building, person=person, orderItems=orderItems, orderAmounts=orderAmounts, ids=ids, numbers=numbers, names=names)

@app.route('/interactiveOrderForm/chooseItem', methods=['POST', 'GET'])
def interactiveOrderFormItem():
    if request.method == 'POST':
        if request.form['click'] == 'Add Item':
            global orderItems, orderAmounts
            orderItems.append(request.form['item'])
            orderAmounts.append(request.form['number'] + " " + request.form['type'])
            return redirect(url_for('interactiveOrderFormCategory'))

        elif request.form['click'] == 'Submit':
            #global orderItems, orderAmounts
            orderItems.append(request.form['item'])
            orderAmounts.append(request.form['number'] + " " + request.form['type'])
            return redirect(url_for('interactiveOrderFormConfirm'))

    return render_template('interactiveOrderFormChooseItem.html', building=building, person=person, category=category, ids=ids, numbers=numbers, names=names, orderItems=orderItems, orderAmounts=orderAmounts, length=length)

@app.route('/interactiveOrderForm/confirm', methods=['POST', 'GET'])
def interactiveOrderFormConfirm():
    global orderItems, orderAmounts
    if request.method == 'POST':
        #Complete Order here
        now = datetime.datetime.now()
        stamp = Delivery.getTimeStamp(now.month, now.day, now.year, now.hour, now.minute, now.second)
        orderNumber = person + '_' + building + '_' + stamp
        itemList = []
        i = 0
        for item in orderItems:
            for item2 in Inventory:
                if item2.id == item:
                    itemList.append((item2.name, orderAmounts[i]))
                    i+=1

        tempLocation = (building, 'Closet')
        newDelivery = Delivery.Delivery(person, orderNumber, itemList, tempLocation, stamp, 'FinishDate')
        pendingDeliveries = []
        pendingDeliveries.append(newDelivery)
        Save.savePendingOrders(pendingDeliveries)

        orderItems = []
        orderAmounts = []

        return redirect(url_for('finishedOrder'))
    return render_template('interactiveOrderFormConfirm.html', building=building, person=person, category=category, ids=ids, numbers=numbers, names=names, orderItems=orderItems, orderAmounts=orderAmounts, length=length)

app.run(host='0.0.0.0', port=8000, threaded=True)
#app.run(debug=True)
