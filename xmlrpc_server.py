import json
import logging
import os
from time import process_time
from converter import convert_to_kml
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Retreive network configutation
HOST =  ''
PORT = 0
with open('config.json') as config_file:
	config = json.load(config_file)
	HOST = config["HOST"]
	PORT = config["PORT"]

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/', '/RPC2', )

# Create a simple XML-RPC server	
server = SimpleXMLRPCServer((HOST, PORT),requestHandler=RequestHandler, logRequests=True)

# KML conversion
# This function explore the directory containig the .json files and
# create the equivalent .kml files and save them in the "Output" directory.
def kml_converter():
	path_to_db = os.path.join(os.getcwd(), 'Data/trajectories')
	path_to_data = os.path.join(os.getcwd(), 'Output')
	files = os.listdir(path_to_db)

	kml_conversion_status = ''
	for file in files:
		if file.endswith('.json'):
			path_to_json = os.path.join(path_to_db, file)
			path_to_kml = os.path.join(path_to_data, file.replace('json', 'kml'))
			t1_start = process_time()
			kml_conversion_status = convert_to_kml(path_to_json, path_to_kml)
			t1_stop = process_time()
			print("Converting time in seconds: {}".format(t1_stop-t1_start))
	return "KML creation compelted!"
# add the kml_converter function to the server registry.
server.register_function(kml_converter)        
try:
    print('Use Control-C to exit')
	# Keep the server listening.
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')