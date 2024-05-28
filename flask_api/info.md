Create Directory flask_basics.
Change directory and Create a file app.py

Create virtual environment
>>>Python -m venv venv

Activate venv
>>>.\venv\Scripts\activate

If needed then select Interpreter
View -> Command Pallate-> Select Interpreter -> Flask_Basics ->venv ->Scripts ->Python.exe

Upgrade pip
>>>python -m pip install --upgrade pip

Install flask
>>>python -m pip install flask

Run the server from terminal
>>>python -m flask run

On command promt (near split window) run following Command
>>>curl -X GET -i -w '\n' localhost:5000 
The -X argument specifies the GET command, and the -i argument displays the header from the response.

