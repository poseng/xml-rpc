# Introduction
The goal of this project was to develop two application servers capable of converting JSON files to KML files.
Python and C++ were chosen for building this two converters. However, due to the lack of library for kml in c++ or probably lack of time
in reviewing the available libkml in C++, only the python converter has been made to the end. 
# Project structure
## Server/Client configuration.
For facilitating the function/method call in the server application, I decided to make a simple XML-RPC (remote procedure call) server that accept function call from client via the XML request. In addition, the problem does not have specific constraint to the type of server and/or request. 
These applications communicate on a 'localhost' and at port 8080.
##




