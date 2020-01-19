# Assignment 2: Create a Server
# By Eduardo Dotel
# CNT 4713 U01
# Note:THIS CODE IS NOT MINE!! Credit: Karim from https://www.afternerd.com/blog/python-http-server/
# I want to create a server that serves a simple website
import http.server
import socketserver
import os
PORT = int(os.environ.get("PORT", 5000))
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()