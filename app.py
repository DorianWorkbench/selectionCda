from flask import Flask, jsonify, request
from controller import CUser

app = Flask(__name__)

@app.route("/", methods=['GET'])
def accueil():
    return jsonify(accueil=True)

@app.route("/inscription", methods=['POST'])
def inscriptionUtilisateur():
    return jsonify(reponse =CUser.ajouterUtilisateur(request))

if __name__ == "__main__":
    app.run(port="3000")