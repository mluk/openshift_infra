from flask import Flask

wurst = Flask(__name__)

@wurst.route("/")
def huhu():
    return "HUHU Schniiiitzellllll"

if(__name__=="__main__"):
    wurst.run()