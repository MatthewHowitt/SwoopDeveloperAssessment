import json
import requests
from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

# This function takes some value as a string, if the string can be converted to an int it does so, otherwise 0 is returned
def convertToInt(string):
	if string:
		try:
			int(string)
			return int(string)
		except ValueError:
			return 0
	return 0

class Math(Resource):
	# Adds two arguments passed as part of the url as n1 and n2
	def get(self):
		n1 = convertToInt(request.args.get('n1'))
		n2 = convertToInt(request.args.get('n2'))
		result = n1 + n2
		return {'result': result}

	# Adds two arguments passed as part of a form as n1 and n2
	def post(self):
		try:
			parser.add_argument('n1', location='form')
			parser.add_argument('n2', location='form')
		except:
			pass
		
		args = parser.parse_args()
		n1 = convertToInt(args['n1'])
		n2 = convertToInt(args['n2'])
		result = n1 + n2

		return {'result':result}

class Airports(Resource):
	# Get a list of airports from a 3rd party service, return error message if call fails
	def get(self):
		try:
			response = requests.get("https://iatacodes.org/api/v6/airports?api_key=472dcce9-ed45-43ec-8492-9cdc10122de9", verify=False)
			return response.json()
		except requests.exceptions.RequestException as e:
			return e

api.add_resource(Math, '/math/add')
api.add_resource(Airports, '/airports')

if __name__ == '__main__':
	app.run(port='5002')