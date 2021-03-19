"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
""" 

import socket,ssl,pprint
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

#create a socket, set hostname = local_name, and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 22000

#check for certification
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations("server_cert.crt")
context.load_cert_chain(certfile="client_cert.crt", keyfile="client_private.pem")

#ssl_sock = ssl.wrap_socket(s)
ssl_sock = context.wrap_socket(s)
ssl_sock.connect((host, port))

#print some usefull info about certificate and connection to client
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())
print ("\nServer authenticated")
print "Server:", ssl_sock.read()

pkey = open("client_private.pem", 'rb').read()
key = RSA.importKey(pkey)

#encrypted AES key
Server_key = ssl_sock.read()
iv = ssl_sock.read()
aes_key = key.decrypt(Server_key)

cipher = AES.new(aes_key, AES.MODE_CBC, iv)
BS = AES.block_size

#PKCS5 padding 
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

#Message to be sent to server encrypted with the AES key
inpt = raw_input('type anything and click enter... ')
ssl_sock.write(cipher.encrypt(pad(inpt)))
print ("\nEncrypted message sent...")
server_encr_message = ssl_sock.read()
print "Server(Undecrypted):",server_encr_message
print "Server:",unpad(cipher.decrypt(server_encr_message))


#colse the socket, connection is terminated  
ssl_sock.close()