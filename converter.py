import simplekml
import json

def convert_to_kml(path_to_json, path_to_data):
	with open(path_to_json) as j_file:
		datas = json.load(j_file)
		kml = simplekml.Kml()
		for data in datas:
			kml.newpoint(name=str(data["id"]),coords=[(data["lng"], data["lat"])])
			kml.save(path_to_data)
		return "New KML file converted and saved at" + str(path_to_data)