from Domain.person import Person
class PersonValidator:
    def __init__(self):
        pass

    def validateNewPerson(self, personList, newPerson):
        for person in personList:
            if person.getID() == newPerson.getID():
                raise ValueError("Enter a unique ID")


def testValidatorPeople():
    person = Person(1, 'Dan', 'Adr')
    personList = []
    personList.append(person)
    val = PersonValidator()
    try:
        val.validateNewPerson(personList, person)
        assert False
    except:
        assert True

testValidatorPeople()