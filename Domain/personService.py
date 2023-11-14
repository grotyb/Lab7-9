from Domain.person import Person
class PersonService:
    def __init__(self, repositoryPeople, validator):
        self.__repo = repositoryPeople
        self.__validator = validator

    def addPerson(self, id, name, adress):
        newPerson = Person(id, name, adress)
        try:
            self.__validator.validateNewPerson(self.__repo.getAllPeople(), newPerson)
            self.__repo.addPerson(newPerson)
            print("Person was saved...")
        except:
            print("Person was not saved, ID must be unique")

    def personDoesExist(self, personID):
        peopleList = self.__repo.getAllPeople()
        for person in peopleList:
            if person.getID() == personID:
                return True
        return False

    def deletePerson(self, idPersonToDelete):
        if self.personDoesExist(idPersonToDelete) == True:
            self.__repo.deletePerson(idPersonToDelete)
            print("Person was deleted...")
        else:
            print("A person with the specified ID does not exist")