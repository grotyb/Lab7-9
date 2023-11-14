from Domain.person import Person
class InMemoryRepositoryPeople:
    def __init__(self):
        self.__peopleList = {}

    def addPerson(self, person):
        self.__peopleList[person.getID()] = person

    def deletePerson(self, personID):
            del self.__peopleList[personID]


    def getAllPeople(self):
        return list(self.__peopleList.values())

    def size(self):
        return len(self.__peopleList)


def testRepoPeople():
    rep = InMemoryRepositoryPeople()
    person1 = Person(1, 'gica', 'vale')
    rep.addPerson(person1)
    assert rep.size() == 1
    rep.deletePerson(1)
    assert rep.size() == 0

testRepoPeople()