from flask import Flask, escape, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello, {escape(name)}!"


@app.route("/hello")
def hello_json():
    d = {"greeting": "hello", "to": "world"}
    return jsonify(d)
