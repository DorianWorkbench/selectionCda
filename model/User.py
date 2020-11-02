from tools import bdd


class User:

    email = ""
    password = ""
    birthDate = ""

    def __init__(self, email, password, birthDate):
        self.email = email
        self.password = password
        self.birthDate = birthDate

    def getEmail(self):
        return self.email

    def getBirthDate(self):
        return self.birthDate

    @staticmethod
    def ajouterUtilisateur(email, password, birthDate):
        bdd.ajouterUtilisateur(email, password, birthDate)
