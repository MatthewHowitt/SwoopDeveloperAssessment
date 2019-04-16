Steps To Run via Command Line:

1. Install Python 3, (3.7.3 was used on my end for testing) using whatever means you choose
2. Run "pip install flask flask_restful" to install dependencies
3. Navigate to the location of api.py and run the api with "python api.py", this will cause the api to start on you local host port 5002 assuming it is free
4. The api can now be reached via http://127.0.0.1:5002/<api>
	Valid api examples:
	GET http://127.0.0.1:5002/math/add$n1=1&n2=1
	POST http://127.0.0.1:5002/math/add
	GET http://127.0.0.1:5002/airports

To Run Tests via Command Line:

1. Run "pip install tavern" to install dependencies
2. Add py.test to path if it is not already there, should be located in Python37/Scripts
3. Navigate to the tests folder and run tests with "py.test -v"
4. You can run individual test files with "py.test <file> -v"

Exceptions To The Requested Deliverable:

I was unable to secure a key from Cirium so I used IATA instead. I am unsure if the IATA endpoint only returns active airports as requested, since it does not seem to track whether or not they are active.