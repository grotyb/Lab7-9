class Person:
    def __init__(self, id, name, adress):
        """
        A person class
        :param id: a unique identifier for each person
        :param name: A name for each person
        :param adress: An adress for each person
        """
        self.__id = id
        self.__name = name
        self.__adress = adress

    def getName(self):
        return self.__name

    def getID(self):
        return self.__id

    def getAdress(self):
        return self.__adress

    def setName(self, newName):
        self.__name = newName

    def setAddress(self, newAddress):
        self.__adress = newAddress

    # def __eq__(self, other):
    #     if self.getID() == other.getID():
    #         return True
    #     return False