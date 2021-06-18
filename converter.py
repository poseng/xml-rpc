import simplekml
import json
import os
def convert_to_kml(path_to_json, path_to_data):
	"""
	This function simply calls the simplekml library for creating a new and simple KML file. 
	"""
	with open(path_to_json) as j_file:
		datas = json.load(j_file)
		kml = simplekml.Kml()
		coordidates = []
		for data in datas:
			pnt = kml.newpoint()
			pnt.name = str(data["id"])
			pnt.description = "Origin: {} and Confiance: {}".format(data["origin"], data["confiance"])
			pnt.coords = [(data["lng"], data["lat"])]
			pnt.style.linestyle.color = simplekml.Color.blue
		kml.save(path_to_data)
		
		return "New KML file converted and saved at" + str(path_to_data)