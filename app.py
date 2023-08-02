from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import spacy

# Simple API to gather relevant data from user input
# Core functionality -> POST http method
# Test functionality -> GET http method


# create instance of the app
app = Flask(__name__)
# create instance of the api
api = Api(app)

static_sentence = {"oraciones": [
 "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
 "San Francisco considera prohibir los robots de entrega en la acera."]}


# load spacy model for nlp
nlp_model = spacy.load("es_core_news_sm")

# We define a class which inherits Resource method from flask_restful module
# By doing this we are able to avoid excesive use of Flask decorators 
# for the endpoints and more centralize in specific functionality

class Sentence(Resource):
	# GET http method working -> just as an example to show desired functionality
	def get(self):
		entities_data = []
		if request.method == "GET":
			for sentence in static_sentence["oraciones"]:
				doc = nlp_model(sentence)
				entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
				entities_data.append(entities)
			return jsonify(entities_data)
	# POST http method working -> simple if statements to handle potential errors
	def post(self):
		if request.method == "POST":
			data = request.get_json() # ensure the input data from user is in json format
			if not data or "oraciones" not in data:
				return jsonify({"error": "Invalid json data"})

			sentences = data["oraciones"] # instanciate the user input 
			results = [] # results from the spacy model predictions

			# Loop through each sentence and perform main functionality
			# which is to extract the entities that appear in the user input
			for sentence in sentences:
				doc = nlp_model(sentence)
				entities = {ent.text: ent.label_ for ent in doc.ents}
				result = {"oracion": sentence,
						 "entidades": entities}
				results.insert(0, result)

				results.append(result)
			return jsonify({"resultado": results})
		
api.add_resource(Sentence, "/")

if __name__ == "__main__":
	app.run(debug=True)
