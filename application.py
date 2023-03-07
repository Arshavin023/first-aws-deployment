from flask import Flask

application = Flask(__name__)
app=application
@app.route('/')
def hello_world():
    return 'My first Web Application deployed on AWS'




