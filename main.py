from flask import Flask

#create app obj
app = Flask(__name__)

#this creates the root end point
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"