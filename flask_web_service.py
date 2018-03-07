from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hi():
    return "Hello, world"

@app.route("/name", methods=["GET"])
def getname():
    name = {
        "name": "Marianne Lee"
    }
    return jsonify(name)

@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    data = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(data)

@app.route("/distance", methods=["POST"])
def distance():
    points = request.get_json()
    dx = points["a"][0]-points["b"][0]
    dy = points["a"][1]-points["b"][1]
    dist = (dx**2 + dy**2)**0.5
    res = {
        "distance": "{}".format(dist),
        "a": "{}".format(points["a"]),
        "b": "{}".format(points["b"]),
    }
    return jsonify(res)
