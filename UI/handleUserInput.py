import datetime


class UserInput:
    def __init__(self):
        pass

    def citireNumarDePersoaneDeAdaugatRandom(self):
        try:
            userInput = int(input("Cate persoane doriti sa adaugati: "))
            return userInput
        except:
            print("Introduceti un numar valid")

    def citireNumarDeEvenimenteDeAdaugatRandom(self):
        try:
            userInput = int(input("Cate evenimente doriti sa adaugati: "))
            return userInput
        except:
            print("Introduceti un numar valid")
    def citireTastaMeniuModificariPeroana(self):
        return self.__readUserInput(2, 1)

    def citireTastaMeniuModificariEvenimente(self):
        return self.__readUserInput(3, 1)

    def citireNumeNou(self):
        newName = input("Intorduceti numele nou dorit: ")
        return newName

    def citireAdresaNoua(self):
        newAddress = input('Introduceti noua adresa: ')
        return newAddress
    def __citireTastaMeniuPrincipal(self):
        """
        Citeste o valoare din intervalul [1,4], numar intreg, altfel va da un ValueError
        :return:
        """
        return self.__readUserInput(8, 1)

    def __citireTastaAditionalaMeniuGesiuni(self):
        """
        Citeste o valoare din intervalul [1,2], numar intreg, altfel va da un ValueError
        :return:
        """
        return self.__readUserInput(2, 1)

    def ___citireValoriAditionaleGestiuniPersoane(self):
        """
        Citeste o valoare din intervalul [1,3], numar intreg, altfel va da un ValueError
        :return:
        """
        return self.__readUserInput(3, 1)

    def __citireValoriAditionaleGestiuniEvenimente(self):
        """
        Citeste o valoare din intervalul [1,3], numar intreg, altfel va da un ValueError
        :return:
        """
        return self.__readUserInput(3, 1)

    def __citireDatePersoana(self):
        """
        Citeste toate datele necesare creeri unei noi persoane
        :return: Un dictionar cu atributele persoanei
        """
        try:
            id = int(input("Introduceti IDul dorit: "))
            nume = input("Introduceti Numele dorit: ")
            adresa = input("Introduceti adresa dorita: ")
            return {'id': id, 'nume': nume, 'adresa': adresa}
        except:
            print("id is invalid")

    def __citireDateEveniment(self):
        """
        Citeste o data
        :return: Datetime datetime object
        """
        id = input("Introduceti IDul dorit: ")
        dataAndHour = self.__citireDataSiOra()
        desc = input("Introduceti descrierea evenimentului: ")
        return {'id': id, 'date': dataAndHour, 'description': desc}

    def citireOra(self):
        """
        Citeste o ora in format hh:mm
        :return: ora ca intreg pozitiv din intervalul [0,24] si minutele intregi pozitivi din intervalul [0,59]
        """
        ora = input("Introduceti ora(hh:mm): ")
        ora = ora.split(':')
        try:
            hour = int(ora[0])
            minutes = int(ora[1])
            if hour < 0 or hour > 24:
                raise Exception("Invalid Hour")
            if minutes < 0 or minutes >= 60:
                raise Exception("Invalid Minutes")
            return {'ora': hour, 'minute': minutes}
        except Exception as ex:
            print(ex)

    def __citireDataSiOra(self):
        dataCitita = self.citireData()
        oraCitita = self.citireOra()
        date = datetime.datetime(dataCitita['an'], dataCitita['luna'], dataCitita['zi'], oraCitita['ora'], oraCitita['minute'])
    def citireData(self):
        try:
            an = int(input("Introduceti anul in care va avea loc evenimentul: "))
            luna = int(input("Introduceti luna in care va avea loc evenimentul: "))
            zi = int(input("Introduceti ziua in care va avea loc evenimentul: "))
            return {'an' : an, 'luna':  luna, 'zi': zi}
        except:
            print("Enter a valid value")
    def readIDForPerson(self):
        try:
            id = int(input("introduceti IDul dorit: "))
            return id
        except:
            print("Invalid id")

    def readIDForEvent(self):
        id = input("introduceti IDul dorit: ")
        return id

    def readEventDescription(self):
        desc = input("Descriere: ")
        return desc

    def citireTastaCautari(self):
        return self.__readUserInput(2, 1)

    def citireTastaRapoarte(self):
        return self.__readUserInput(4, 1)
    def citireDateParticipare(self):
        try:
            personID = int(input("Introduceti IDul persoanei pe care doriti sa o inscrieti la un eveniment:"))
            eventID = input("Introduceti IDul evenimentului la care doriti sa participe: ")
            return {'idPerson': personID, 'idEvent': eventID}
        except:
            print("person ID mut be an int")


    def citireIDPersoana(self):
        try:
            id = int(input("Introuceti IDul persoanei: "))
            return id
        except:
            print("Id mut be an integer")
            return None
    def __readUserInput(self, maxInput, lowerBoundInput):
        """
        A function that prompts the user to input a value and validates that it is an int and that it is contained between the lower and upper bound
        :param maxInput: Upper bound for input(as an int)
        :param lowerBoundInput: Lower bound for input(as an int)
        :return: The user input
        """
        try:
            userInput = int(input("Introduceti tasta dorita: "))
            if userInput < lowerBoundInput or userInput > maxInput:
                raise ValueError("Input is not in range")
            return userInput
        except ValueError as ex:
            print(ex)
        except:
            print("Intoduceti o valoare corecta")
