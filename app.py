from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def test():
    return jsonify(test="true")

if __name__ == "__main__":
    app.run(port="3000")