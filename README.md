# Introduction
The goal of this project was to develop two application servers capable of converting JSON files to KML files.
Python and C++ were chosen for building this two converters. However, due to the lack of library for kml in c++ or probably lack of time
in reviewing the available libkml in C++, only the python converter has been made to the end. 
# Project structure
## Server/Client configuration.
For facilitating the function/method call in the server application, I decided to make a simple XML-RPC (remote procedure call) server that accept function call from client via the XML request. In addition, the problem does not have specific constraint to the type of server and/or request. 
These applications communicate on a 'localhost' and at port 8080.
### Usage
Run : python3 xmlrpc_server.py and python3 xmlrpc_client.py
## Architecture
I imagined that the server side program could (re)-generate/convert a set of JSON file in a directory and save them into another directory called "Output". This approach is ideal for a specific traj.json file, yet I consider it is very convenvient to automate the conversion. 
## Libraries
Beside from the standard json library/package in Python3, I needed to install the simplekml package that is simple as its name, yet a best python API for KML. 
# Duration
I had approximately spent 8 to 10 hours on this project. Nonetheless, most of the time was for literature review of the library and the structure of KML data. 




