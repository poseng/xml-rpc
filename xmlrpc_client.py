import xmlrpc.client
proxy = xmlrpc.client.ServerProxy('http://localhost:8080')
print(proxy.kml_converter())