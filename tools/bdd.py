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

def ajouterUtilisateur(email, password, birthDate):
    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "INSERT INTO User(email, password, birthDate) VALUES (%s, %s, %s)"

    utilisateur = (email, password, birthDate)
    cursor.execute(sql, utilisateur)

    connexion.commit()
    cursor.close()
    connexion.close()

    print("Création d'utilisateur faite")