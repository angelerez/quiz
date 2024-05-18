from flask import Flask

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

    #check if quiz exists 
        #if so return the relevant info 
        #else throw an error 
    x = 1 