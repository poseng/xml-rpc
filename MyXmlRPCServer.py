import os
import json
import simplekml
from converter import convert_to_kml
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/', '/RPC2', )
	# restrcited access to data dir that store trajectory in json

# Create server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
	server.register_introspection_functions()
	# # Register pow() function; this will use the value of pow.__name__ as the name, which is just 'pow'.
	# server.register_function(pow)
	# Register a function under a different name
	def adder_function(x, y):
		return x + y
	server.register_function(adder_function, 'add')

	def kml_converter():
		path_to_db = os.path.joint(os.getcwd(), 'DB')
		path_to_data = os.path.join(os.getcwd(), 'Data')
		files = os.listdir(path_to_db)

		kml_conversion_status  = ''
		for file in files:
			if file.endswith('.json'):
				path_to_json = os.path.join(path_to_db, file)
				path_to_kml = os.path.join(path_to_data, file.replace('json', 'kml'))
				kml_conversion_status = convert_to_kml(path_to_json, path_to_kml)
		return kml_conversion_status

	server.register_function(kml_converter, 'kml_converter')
	# # Register an instance; all the method for the instance are published.
	# # public as XML-RPC method
	# class MyFuncs:
	# 	def mul(self, x, y):
	# 		return x * y
	# server.register_instance(MyFuncs())

	# Run the server's main loop
	server.serve_forever()