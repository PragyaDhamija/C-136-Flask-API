from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

def HomePage():
    return jsonify({"data":data,"message":"Success!"}),200

@app.route("/planet")

def PlanetData():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({"data":planet_data, "Message":"Data Shown!!!"}),200

if(__name__ == "__main__"):
    app.run(debug=True)

