from flask import Flask
from flask import Response
import json 
from flask import jsonify

#create app obj
app = Flask(__name__)

#this creates the root end point
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#/quiz/get/biology 
    # name = biology
#get quiz data
@app.route("/quiz/get/<name>", methods = ["GET"])
def get_quiz(name): 
    
    #try catch to deal with bad name
    try: 
        #open the file
        f = open("./Qs/"+name+".json")
    except FileNotFoundError: 
        #if name not found pass a special message to the front end
        return {"message": "FileNotFound"}
    
    #load the actual json data
    obj = json.load(f)
    
    #return the json data
    return obj
