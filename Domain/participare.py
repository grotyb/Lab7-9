import copy
class Participa:
    def __init__(self, eventID, personID):
        self.__eventID = eventID
        self.__personID = personID

    def getEventID(self):
        return self.__eventID

    def getPersonID(self):
        persIDCopy = copy.deepcopy(self.__personID)
        return persIDCopy

def testParticipa():
    p = Participa("eh", 3)
    assert p.getEventID() == "eh"
    assert p.getPersonID() == 3

testParticipa()