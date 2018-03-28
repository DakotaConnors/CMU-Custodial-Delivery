class Delivery:
    def __init__(self, person, number, items, location, timeStampCreate, timeStampComplete):
        self.person = person
        self.number = number
        self.items = items # list of [item:string, numberOfItem:string]
        self.location = location # pair of values (Building, 'Closet')
        self.createDate = timeStampCreate
        self.completeDate = timeStampComplete
        #self.createDate = (str(CurrentTime.month) + '/' + str(CurrentTime.day) + '/' + str(CurrentTime.year)
        #self.completeDate = (str(CurrentTime.month) + '/' + str(CurrentTime.day) + '/' + str(CurrentTime.year)
        self.staged = False

def getTimeStamp(month, day, year, hour, minute, second):
    timeStamp = "" #MM/DD/YYYY/HOUR/MINUTE/SECOND
    timeStamp += str(month) + '-'
    timeStamp += str(day) + '-'
    timeStamp += str(year) + '-'
    timeStamp += str(hour) + '-'
    timeStamp += str(minute) + '-'
    timeStamp += str(second) + '-'
    return timeStamp

def printTimeStamp(stamp):
    timeStrings = stamp.split('-')
    timeStamp = timeStrings[0] + '/'
    timeStamp += timeStrings[1] + '/'
    timeStamp += timeStrings[2] + ' '
    timeStamp += timeStrings[3] + ':'
    timeStamp += timeStrings[4] + ':'
    timeStamp += timeStrings[5]
    return timeStamp
