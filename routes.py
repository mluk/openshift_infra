from flask import Flask
import os

wurst = Flask(__name__)

@wurst.route("/")
def index():
    return "Wurssst"

if __name__=="__main__":
    wurst.run()
#    wurst.run(host="127.0.0.1", port=8080)
