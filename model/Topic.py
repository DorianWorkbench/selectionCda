from tools import bdd
from model.User import User
class Topic:

    title = ""
    categorie = ""
    user = User("","","")

    def __init__(self, title, categorie, user):
        self.title = title
        self.categorie = categorie
        self.user = user

    @staticmethod
    def listeTitreTopic():
        return bdd.listeTitreTopic()

    @staticmethod
    def creationTopic(title, idCategory, idUser):
        return bdd.creationTopic(title, idCategory, idUser)

    @staticmethod
    def supressionTopic(idTopic):
        return bdd.supressionTopic(idTopic)

    @staticmethod
    def miseAjourTopic(idTopic, title):
        return bdd.miseAjourTopic(idTopic,title)