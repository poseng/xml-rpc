import xmlrpc.client
import os
proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
# print(proxy.list_contents(os.getcwd()))
print(proxy.kml_converter())