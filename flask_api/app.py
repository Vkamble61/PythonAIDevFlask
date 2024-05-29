from flask import Flask, make_response, request
app = Flask(__name__)
#Following data is genrated by  Mockaroo.
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

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
#>>>curl -X GET -i -w '\n' localhost:5000/no_content

#Send custom HTTP code back with the make_response() method. Import make_response() 
@app.route("/exp")
def index_explicit():
    resp = make_response({"Message": "Hello World"})
    resp.status_code = 200
    return resp

#Test the server
#>>>curl -X GET -i -w '\n' localhost:5000/exp
#The output similar to --> status of 200, Content-Type of application/json, and JSON output of {"message": "Hello World"}:

#create an end point that returns the person’s data to the client in JSON format.
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message":f"Data of length {len(data)} found"}
        else:
            return ({"message":"Data is empty"}, 500)
    except NameError:
        return ({"message": "Data not found"}, 404)
    
#test the endpoint
#>>>curl -X GET -i -w '\n' localhost:5000/data

#import request
@app.route("/name_search")
def name_search():
    query = request.args.get("q")
    
    if not query:
        return ({"message":"Invalid input parameter"}, 422)
        
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return ({"message":"person not found"}, 404)

#test the endpoint
#JSON output of person with first name Tanya:
#>>>curl -X GET -i -w '\n' localhost:5000/name_search?q=Tanya 
# the method returns HTTP 422 if the argument q is missing
#>>>curl -X GET -i -w '\n' "localhost:5000/name_search" 
# the first_name is not present in our list of people: message: Person not found will be displayed
#>>>curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"

#count
@app.route("/count")
def count():
    try: 
        return ({"data count": len(data)}, 200)
    except NameError:
        return ({"message":"data not defined"}, 500)

#Test endpoint
#>>>curl -X GET -i -w '\n' "localhost:5000/count"

#find by uuid
@app.route("/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            return person
    return ({"message":"person not found"},404)        

#Test 
#curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287

#Delete
@app.route("/person/<uuid:id>", methods=['DELETE'])
def delete_by_uuid(id):
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message":f"{id}"}, 200
    return {"message": "person not found"}, 404
#>>>curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111

#add user
@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500
    return {"message": f"{new_person['id']}"}, 200

#curl -X POST -i -w '\n' --url http://localhost:5000/person   --header 'Content-Type: application/json' \
# --data '{
#        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
#        "first_name": "John",
#        "last_name": "Horne",
#        "graduation_year": 2001,
#        "address": "1 hill drive",
#        "city": "Atlanta",
#       "zip": "30339",
#        "country": "United States",
#        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
#}'

#curl -X POST -i -w '\n'   --url http://localhost:5000/person   --header 'Content-Type: application/json'   --data '{}'
#Error handler
@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404
#>>>curl -X POST -i -w '\n' http://localhost:5000/notvalid
#