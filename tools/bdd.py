import mysql.connector as MC

def connexionBdd():
    try:
        connexion = MC.connect(
            host="localhost",
            user = "root",
            password="",
            database="selectioncda"
        )
        print("Vous êtes connecté")
        return connexion

    except MC.errors as err:
        print(err)

