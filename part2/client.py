"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
""" 

import socket,ssl,pprint

#create a socket, set hostname = local_name, and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 22000

#check for certification
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations("cert.pem")

#ssl_sock = ssl.wrap_socket(s)
ssl_sock = context.wrap_socket(s,server_hostname="Minas")
ssl_sock.connect((host, port))

#print some usefull info about certificate and connection to client
print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())
print ("\nServer authenticated")
print "Server:", ssl_sock.read()

#Message to be sent to server
inpt = raw_input('type anything and click enter... ')
ssl_sock.write(inpt)

#colse the socket, connection is terminated  
ssl_sock.close()
