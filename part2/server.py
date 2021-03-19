"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
""" 

import socket, ssl
from timeit import default_timer as timer

#create a socket, set hostname = local_name, and port
#bind them to the socket and start listening for clients
s = socket.socket()
host = socket.gethostname()
port = 22000
s.bind((host,port))
s.listen(5)

#read data the client sends
def read_data(connstream, data):
    print "Client:", data
    return False

#try to interact with client
def interact(connstream):
    data = connstream.read()
    # null data means the client is finished with us
    while data:
        if not read_data(connstream, data):
            # we'll assume read_data returns False
            # when we're finished with client
            break
        data = connstream.read()
        # finished with client
    

start = timer()
#wait for 10 seconds and listen to any client who wants to connect
while (timer()-start) <= 10:
    newsocket, addr = s.accept()
    #set connection using the certificate of server
    connstream = ssl.wrap_socket(newsocket,server_side=True,certfile="cert.pem",keyfile="key.pem")
    print("\nCertificate send...")
    print("Connection accepted from " + repr(addr[1]))

    connstream.write("approved connection\n")
    try:
        interact(connstream)
    finally: 
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
        
print ("\nConnection Closed!")



    

  