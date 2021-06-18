import simplekml
import json
import os
def convert_to_kml(path_to_json, path_to_data):
	with open(path_to_json) as j_file:
		datas = json.load(j_file)
		kml = simplekml.Kml()
		ls = kml.newlinestring(name="Trajecotry")
		coordidates = []
		for data in datas:
			coordidates.append((data["lng"], data["lat"]))
		ls.coords = coordidates
		ls.extrude = 1
		ls.altitudemode = simplekml.AltitudeMode.relativetoground
		ls.style.linestyle.width = 5
		ls.style.linestyle.color = simplekml.Color.blue
		kml.save(path_to_data)
		#ml.newpoint(name=str(data["id"]),coords=[(data["lng"], data["lat"])])
		# kml.save(path_to_data)
		return "New KML file converted and saved at" + str(path_to_data)