from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ex")
def extent():
    return "<p>Extended</p>"  

@app.route("/new")
def extent2():
    return "<p>1stbranch</p>"       