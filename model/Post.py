from tools import bdd
from model.Topic import Topic
from model.User import User
class Post:

    topic = Topic("",None,None)
    user = User("","","")
    postDate = ""
    content = ""

    def __init__(self, postDate, content, topic, user):
        self.topic = topic
        self.user = user
        self.postDate = postDate
        self.content = content


    @staticmethod
    def creationPost(content, idTopic, idUser):
        return bdd.creationPost(content, idTopic, idUser)

    @staticmethod
    def listePost(idTopic):
        return bdd.listePost(idTopic)

    @staticmethod
    def suppressionPost(idPost):
        return bdd.suppressionPost(idPost)

    @staticmethod
    def miseAjourPost(idPost, content):
        return bdd.miseAjourPost(idPost, content)
