from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!!"
#Test the endpoint 
#>>>python -m flask run
#>>>curl -X GET -i -w '\n' localhost:5000

