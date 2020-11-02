from flask import Flask, jsonify, request
from controller import CUser,CTopic, CPost, CCategory

app = Flask(__name__)

@app.route("/", methods=['GET'])
def accueil():
    return jsonify(accueil="Vous êtes connecté")

#Utilisateur
@app.route("/inscription", methods=['POST'])
def inscriptionUtilisateur():
    return jsonify(reponse=CUser.ajouterUtilisateur(request))


#Topic
@app.route("/creationTopic", methods=['POST'])
def creationTopic():
    return jsonify(reponse=CTopic.creationTopic(request))

@app.route("/supressionTopic", methods=['DELETE'])
def supressionTopic():
    return jsonify(reponse=CTopic.supressionTopic(request))

@app.route("/miseAjourTopic", methods=['PUT'])
def miseAjourTopic():
    return jsonify(reponse=CTopic.miseAjourTopic(request))

@app.route("/listeTitreTopic", methods=['GET'])
def listeTitreTopic():
    return jsonify(listeTitre=CTopic.listeTitreTopic())


#Post
@app.route("/creationPost", methods=['POST'])
def creationPost():
    return jsonify(reponse= CPost.creationPost(request))

@app.route("/listePost", methods=['GET'])
def listePost():
    return jsonify(posts= CPost.listePost(request))

@app.route("/suppressionPost", methods=['DELETE'])
def suppressionPost():
    return jsonify(reponse = CPost.suppressionPost(request))

@app.route("/miseAjourPost", methods=['PUT'])
def miseAjourPost():
    return jsonify(reponse= CPost.miseAjourPost(request))

#Category
@app.route("/creationCategory", methods=['POST'])
def creationCategory():
    return jsonify(reponse = CCategory.creationCategory(request))

if __name__ == "__main__":
    app.run(port="3000")