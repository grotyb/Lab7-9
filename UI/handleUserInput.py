import datetime


class UserInput:
    def __init__(self):
        pass

    def __citireTastaMeniuPrincipal(self):
        """
        Citeste o valoare din intervalul [1,4], numar intreg, altfel va da un ValueError
        :return:
        """
        return self.__readUserInput(4, 1)

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
        dataAndHour = self.__citireData()
        desc = input("Introduceti descrierea evenimentului: ")
        return {'id': id, 'date': dataAndHour, 'description': desc}

    def __citireOra(self):
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
            return hour, minutes
        except Exception as ex:
            print(ex)
    def __citireData(self):
        try:
            an = int(input("Introduceti anul in care va avea loc evenimentul: "))
            luna = int(input("Introduceti luna in care va avea loc evenimentul: "))
            zi = int(input("Introduceti ziua in care va avea loc evenimentul: "))
            ora = self.__citireOra()
            date = datetime.datetime(an, luna, zi, ora[0], ora[1])
            return date
        except:
            print("Enter a valid value")
    def readIDForDeletionPerson(self):
        try:
            id = int(input("introduceti IDul pe care doriti sa o stergeti: "))
            return id
        except:
            print("Invalid id")

    def readIDForDeletionEvent(self):
        id = input("introduceti IDul pe care doriti sa o stergeti: ")
        return id

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
