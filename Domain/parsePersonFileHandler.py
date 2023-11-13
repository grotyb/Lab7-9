from UTILS import readFileHandler
import os
def parsePersonFile():
    absolutePath = os.path.dirname(__file__)
    relativePath = '../Data/persoane.txt'
    fullPath = os.path.join(absolutePath, relativePath)
    fileContent = readFileHandler.readFile(fullPath)
    print(fileContent)
    peopleData = extractPeopleData(fileContent)


def extractPeopleData(fileContent):
    """
    Primeste o lista care contine pe fiecare pozitie o linie din fisierul persoane.txt
    fiecare linie trebuie sa aiba formatul: ID,Nume,Tara,Judet,Oras,Strada,numar
    :param fileContent: O lista care contine pe fiecare pozitie o linie din fisierul persoane.txt
    :return: o lista de dictionare in
    """
    people = []
    for fileLine in fileContent:
        people.append(fileLine.split(','))
    for person in people:
        person[6] = person[6][:-1]
    for person in people:
        person = createPerson(people)
def testExtractPeopleData():
    assert extractPeopleData(['1,Dan,Romania,Cluj-Napoca,Cluj,Oasului,14\n', '2,Iris,Romania,Cluj-Napoca,Cluj,Dimitrie Bolintineanu,5\n']) == [
               {'ID': '1', 'Nume': 'Dan', 'Judet': 'Cluj-Napoca', 'Oras': 'Cluj', 'Strada': 'Oasului', 'numar': 14},
               {'ID': '2', 'Nume': 'Iris', 'Judet': 'Cluj-Napoca', 'Oras': 'Cluj', 'Strada': 'Dimitrie Bolintineanu','numar': 5}]
    assert extractPeopleData(['1,Dan,Romania,Cluj-Napoca,Cluj,Oasului,14\n']) == [{'ID': '1', 'Nume': 'Dan', 'Judet': 'Cluj-Napoca', 'Oras': 'Cluj', 'Strada': 'Oasului', 'numar': 14}]

testExtractPeopleData()
parsePersonFile()