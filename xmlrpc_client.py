import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# print(s.pow(2, 3))
print(s.add(2, 3))
# print(s.mul(5, 2))
# print(s.convert('traj1.kml'))
# print(s.kml_converter("traj1.kml"))
# print(s.kml_converter())
s.kml_converter()
# s.convert('traj1.kml')
# print(s.system.listMethods())
