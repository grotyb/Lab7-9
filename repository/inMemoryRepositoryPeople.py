from repository.validator import Validator
from Domain.person import Person
class InMemoryRepositoryPeople:
    def __init__(self):
        self.__peopleList = {}
        self.__validator = Validator

    def addPerson(self, person):
        try:
            self.__validator.validateNewPerson(self, self.getAllPeople(), person)
            self.__peopleList[person.getID()] = person
        except ValueError as ex:
            print(ex)

    def deletePerson(self, personID):
        foundPersonWithID = False
        for ID in self.__peopleList:
            if ID == personID:
                foundPersonWithID = True
        if foundPersonWithID:
            del self.__peopleList[personID]

    def personDoesExist(self, personID):
        peopleList = self.getAllPeople()
        for person in peopleList:
            if person.getID() == personID:
                return True
        return False
    def getAllPeople(self):
        return list(self.__peopleList.values())

    def size(self):
        return len(self.__peopleList)


def testRepoPeople():
    rep = InMemoryRepositoryPeople()
    person1 = Person(1, 'gica', 'vale')
    rep.addPerson(person1)
    assert rep.size() == 1
    assert rep.personDoesExist(1)
    rep.deletePerson(1)
    assert rep.size() == 0

testRepoPeople()