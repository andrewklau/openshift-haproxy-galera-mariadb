import sys
import os
import socket
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

def get_lock(process_name):
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_socket.bind('\0' + process_name)
        print 'Starting..'
    except socket.error:
        print 'Lock exists..'
        sys.exit()

get_lock('running_test')
while True:

	HandlerClass = SimpleHTTPRequestHandler
	ServerClass  = BaseHTTPServer.HTTPServer
	Protocol     = "HTTP/1.0"

	host = os.environ.get('OPENSHIFT_HAPROXYMARIADB_HOST')
	port = os.environ.get('OPENSHIFT_HAPROXYMARIADB_META_PORT')
        server_address = (host, port)

	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)

	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "..."
	httpd.serve_forever()

