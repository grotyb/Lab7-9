import os
class ReadFromFile:
    def __init__(self, fileName):
        """
        :param fileName: absoulute or relative path to the file
        """
        self.__fileName = fileName
        self.__textData = self.__readFile(self.__fileName)

    def getTextData(self):
        """
        A method that returns all the lines of the specified file as an array without endline characters and empty lines
        :return: an array with the file lines
        """
        return self.__textData
    def __readFile(self, fileName):
        file = open(fileName)
        fileContent = file.readlines()
        fileContent = self.__removeEmptyLines(fileContent)
        fileContent = self.__removeEndLineCharacterFromLines(fileContent)
        return fileContent

    def __removeEmptyLines(self, fileContent):
        index = 0
        while index < len(fileContent):
            if fileContent[index] == '\n':
                del fileContent[index]
                index -= 1
            index += 1
        return fileContent

    def __removeEndLineCharacterFromLines(self, fileContent):
        for index in range(len(fileContent)):
            fileContent[index] = fileContent[index][:-1]
        return fileContent