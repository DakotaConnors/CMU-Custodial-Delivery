import pickle
def save(order):
    output_file = open("orders.bin", "wb")
    #print('saving')
    pickle.dump(order, output_file)
    output_file.close()

def loadCurrentDeliveries():
    input_file = open("currentOrders.bin", "rb")
    try:
        currentOrders = pickle.load(input_file)
    except (EOFError):
        currentOrders = "NO CURRENT ORDERS"
    return currentOrders
