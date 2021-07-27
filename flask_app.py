from flask import Flask

app = Flask(__name__)

@app.route("/app")
@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"
