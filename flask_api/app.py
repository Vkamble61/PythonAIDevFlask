from flask import Flask, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!!"
#Test the endpoint 
#>>>python -m flask run
#>>>curl -X GET -i -w '\n' localhost:5000

#Set response status code
@app.route("/no_content")
def no_content():
    """This function returns No content found message """
    # Even though you returned a JSON message, it is not sent back to 
    # the client as 204. By default, nothing is returned.
    return ({"Message":"No Content Found"},204)
#Test the endpoint 
#curl -X GET -i -w '\n' localhost:5000/no_content

#Send custom HTTP code back with the make_response() method. Import make_response() 
@app.route("/exp")
def index_explicit():
    resp = make_response({"Message": "Hello World"})
    resp.status_code = 200
    return resp

#Test the server
#curl -X GET -i -w '\n' localhost:5000/exp
#The output similar to --> status of 200, Content-Type of application/json, and JSON output of {"message": "Hello World"}:

