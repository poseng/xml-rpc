import logging
import os
from time import process_time
from converter import convert_to_kml
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/', '/RPC2', )
	# restrcited access to data dir that store trajectory in json
	
server = SimpleXMLRPCServer(('localhost', 9000),requestHandler=RequestHandler, logRequests=True)

# Expose a function
def list_contents(dir_name):
	logging.debug('list_contents(%s)', dir_name)
	return os.listdir(dir_name)


server.register_function(list_contents)

# KML conversion
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
server.register_function(kml_converter)        
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')