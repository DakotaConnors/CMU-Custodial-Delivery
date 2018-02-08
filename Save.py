import pickle
def save(Buildings):
    output_file = open("tempSave.bin", "wb")
    print('saving')
    pickle.dump(Buildings, output_file)
    output_file.close()

def load():
    input_file = open("tempSave.bin", "rb")
    print('loading')
    Buildings = pickle.load(input_file)
    input_file.close()
    return Buildings
