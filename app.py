from flask import Flask, jsonify, request
from controller import CUser,CTopic
app = Flask(__name__)

@app.route("/", methods=['GET'])
def accueil():
    return jsonify(accueil=True)

@app.route("/inscription", methods=['POST'])
def inscriptionUtilisateur():
    return jsonify(reponse =CUser.ajouterUtilisateur(request))

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

@app.route("/creationPost", methods=['POST'])
def creationPost():
    return jsonify()

if __name__ == "__main__":
    app.run(port="3000")