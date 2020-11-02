from tools import bdd
class Category:

    label = ""

    def __init__(self, label):
        self.label = label

    @staticmethod
    def creationCategorie(label):
        return bdd.creationCategorie(label)