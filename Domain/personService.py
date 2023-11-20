from Domain.person import Person
import random
import string
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

    def modifyPersonName(self, idPerson, newName):
            if self.__repo.find(idPerson) != None:
                self.__repo.modifyPersonName(newName, idPerson)
            else:
                print("Acest ID nu exista, nu se poate modifica numele")

    def cautaDupaId(self, id):
        if self.personDoesExist(id) == True:
            personList = self.__repo.getAllPeople()
            for person in personList:
                if person.getID() == id:
                    return person
        else:
            print("A person with the specified ID does not exist")


    def modifyPersonAddress(self, idPerson, newAddress):
        if self.__repo.find(idPerson) != None:
            self.__repo.modifyPersonAddress(newAddress, idPerson)
        else:
            print("Acest ID nu exista, nu se poate modifica adresa")

    def addRandomPeople(self, nrOfPeople):
        """
        O metoda care adauga in repository nrOfPeople persoane
        :param nrOfPeople: Numar natural pozitiv
        :return: None
        """
        i = 0
        minRandID = self.__getMaxID()
        maxRandID = self.__getMaxID() + nrOfPeople + 100
        while i < nrOfPeople:
            studId = random.randint(minRandID, maxRandID)
            studName = "".join(random.choices(string.ascii_lowercase, k=5))
            studAddress = "".join(random.choices(string.ascii_lowercase, k=10))
            randPers = Person(studId, studName, studAddress)
            try:
                self.__validator.validateNewPerson(self.__repo.getAllPeople(), randPers)
                self.__repo.addPerson(randPers)
                i+=1
            except:
                pass


    def __getMaxID(self):
        listaPersoane = self.__repo.getAllPeople()
        maxID = 0
        for person in listaPersoane:
            if person.getID() > maxID:
                maxID = person.getID()
        return maxID

    def deletePerson(self, idPersonToDelete):
        if self.personDoesExist(idPersonToDelete) == True:
            self.__repo.deletePerson(idPersonToDelete)
            print("Person was deleted...")
        else:
            print("A person with the specified ID does not exist")

def testPersonService():
    from repository.inMemoryRepositoryPeople import InMemoryRepositoryPeople
    from repository.validatorPeople import PersonValidator
    rep = InMemoryRepositoryPeople()
    val = PersonValidator()
    srv = PersonService(rep, val)
    persDeTest = Person(1, "lica", "Samadaul")
    srv.addPerson(persDeTest.getID(), persDeTest.getName(), persDeTest.getAdress())
    assert srv.cautaDupaId(1) == persDeTest
    assert srv.cautaDupaId(2) == None

# testPersonService()
