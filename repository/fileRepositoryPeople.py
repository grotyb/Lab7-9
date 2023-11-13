from repository.inMemoryRepositoryPeople import InMemoryRepositoryPeople
from Domain.person import Person
from UTILS.readFileHandler import ReadFromFile
from repository.validator import Validator
class FileRepoPeople(InMemoryRepositoryPeople):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__loadFromFile(fileName)
        self.__validator = Validator()


    def __loadFromFile(self, fileName):
        fileText = ReadFromFile(fileName)
        fileText = fileText.getTextData()
        peopleList = self.__parseTextLineIntoPerson(fileText)
        self.__save(peopleList)

    def __parseTextLineIntoPerson(self, textLines):
        personList = []
        for textLine in textLines:
            textLine = textLine.split(',')
            id = textLine[0]
            nume  = textLine[1]
            adresa = textLine[2]
            person = Person(id, nume, adresa)
            personList.append(person)
        return personList

    def addPerson(self, person):
        InMemoryRepositoryPeople.addPerson(self, person)
        self.__loadToFile(InMemoryRepositoryPeople.getAllPeople(self))
            # addToFile

        #TODO -> Add new person to file

    def __loadToFile(self, peopleList):
        f = open(self.__fileName, "w")
        for person in peopleList:
            stringToWrite = self.__parsePersonIntoTextLine(person)
            stringToWrite += '\n'
            f.write(stringToWrite)
        f.close()
    def __parsePersonIntoTextLine(self, person):
        personString = ""
        personString += person.getID()
        personString += ","
        personString += person.getName()
        personString += ","
        personString += person.getAdress()
        return personString

    def deletePerson(self, personID):
        InMemoryRepositoryPeople.deletePerson(self, personID)
        peopleList = InMemoryRepositoryPeople.getAllPeople(self)
        self.__loadToFile(peopleList)
    def __save(self, peopleList):
        for people in peopleList:
            InMemoryRepositoryPeople.addPerson(self, people)