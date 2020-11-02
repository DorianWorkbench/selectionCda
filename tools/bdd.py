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

#Utilisateur
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

#Topic
def verificationTopic(title):
    connexionVerif = connexionBdd()
    cursorVerif = connexionVerif.cursor()
    try:
        sqlVerif = "SELECT title FROM Topic WHERE title = '"+title+"'"

        cursorVerif.execute(sqlVerif)
        resultat = cursorVerif.fetchall()

        if (len(resultat)>=1):
            print("Votre topic existe déjà")
            return False
        else:
            print("Le topic n'existe pas")
            return True

    except:
        print("erreur")
        return False
    finally:
        cursorVerif.close()
        connexionVerif.close()


def creationTopic(title, idCategory, idUser):
    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "INSERT INTO Topic(title, idCategory, idUser) VALUES(%s, %s, %s)"
    topic = (title, idCategory, idUser)
    connexion.commit()

    if verificationTopic(title):
        cursor.execute(sql, topic)
        cursor.close()
        connexion.close()
        etat = True

    else:
        cursor.close()
        connexion.close()
        etat = False

    return etat

def suppressionPostTopic(idTopic):
    connexionPostTopic = connexionBdd()
    cursorPostTopic = connexionPostTopic.cursor()


    sql="DELETE FROM Post WHERE idTopic = "+idTopic+""
    cursorPostTopic.execute(sql)
    connexionPostTopic.commit()

    print("post supprimé pour l'id : "+idTopic)

    cursorPostTopic.close()
    connexionPostTopic.close()

def supressionTopic(idTopic):
    connexion = connexionBdd()
    cursor = connexion.cursor()

    suppressionPostTopic(idTopic)

    sql = "DELETE FROM Topic WHERE id = "+idTopic+""

    cursor.execute(sql)
    connexion.commit()

    cursor.close()
    connexion.close()

    return True

def miseAjourTopic(idTopic, title):

    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "UPDATE Topic SET title = '"+title+"' WHERE id = "+idTopic+""

    cursor.execute(sql)
    connexion.commit()

    cursor.close()
    connexion.close()

    return True

def listeTitreTopic():

    connexion = connexionBdd()
    cursor = connexion.cursor()

    listeTitre = []
    sql = "SELECT title FROM Topic"

    cursor.execute(sql)

    resultats = cursor.fetchall()
    for result in resultats:
        listeTitre.append(result[0])

    cursor.close()
    connexion.close()

    return listeTitre

#Post
def creationPost(content, idTopic, idUser):

    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "INSERT INTO Post(postDate, content, idTopic, idUser) VALUES(NOW(), %s, %s, %s)"

    post = (content, idTopic, idUser)

    cursor.execute(sql, post)
    connexion.commit()

    cursor.close()
    connexion.close()

    return True

def listePost(idTopic):

    connexion = connexionBdd()
    cursor = connexion.cursor()
    listePost = []
    sql = "SELECT * FROM post WHERE idTopic = "+idTopic+""

    cursor.execute(sql)

    resultats = cursor.fetchall()

    for result in resultats:
        listePost.append(result)

    cursor.close()
    connexion.close()

    return listePost

def suppressionPost(idPost):

    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "DELETE FROM Post WHERE id = "+idPost+""

    cursor.execute(sql)
    connexion.commit()

    cursor.close()
    connexion.close()

    return True

def miseAjourPost(idPost, content):

    connexion = connexionBdd()
    cursor = connexion.cursor()

    sql = "UPDATE post SET content = '"+content+"' WHERE id = "+idPost+""

    cursor.execute(sql)
    connexion.commit()

    cursor.close()
    connexion.close()

    return True
