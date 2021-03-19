"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
""" 
import os
from Crypto.PublicKey import RSA
from timeit import default_timer as timer
from Crypto.Cipher import AES
import socket,ssl,pprint
from OpenSSL.crypto import dump_privatekey, FILETYPE_ASN1
from Crypto.Util.asn1 import DerSequence
from OpenSSL import crypto as c


#create a socket, set hostname = local_name, and port
#binf them to the socket and start listening for clients
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 22000

s.bind((host,port))
s.listen(5)

#check for certification
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations("client_cert.crt")
context.load_cert_chain(certfile="server_cert.crt", keyfile="server_private.pem")

#after authentication we extract public_key from certificate
cert = c.load_certificate(c.FILETYPE_PEM, file("client_cert.crt").read())
pkey = cert.get_pubkey()
src = dump_privatekey(FILETYPE_ASN1, pkey)
pub_der = DerSequence()
pub_der.decode(src)
pub_key = RSA.construct((long(pub_der._seq[1]), long(pub_der._seq[2])))


def encrypt_aes_key(aes_key):  
    encrypted_aes_key = pub_key.encrypt(aes_key,32)[0]
    return encrypted_aes_key

def generate_AES_key():
    return os.urandom(16)

#generate and encrypt the aes key for symmetric encryption
iv = os.urandom(16)
aes_key = generate_AES_key()
encrypted_aes_key = encrypt_aes_key(aes_key)

cipher = AES.new(aes_key, AES.MODE_CBC, iv)
BS = AES.block_size

#PKCS5 padding 
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

#read data the client sends
def read_data(connstream, data):
    prin = unpad(cipher.decrypt(data))
    print "Client(Undecrypted):", data
    print "Client:", prin
    return False

#try to interact with client
def interact(connstream, cipher):
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
    connstream = context.wrap_socket(newsocket,server_side=True)
    
    #print some usefull info about certificate and connection to client
    print connstream.cipher()
    print pprint.pformat(connstream.getpeercert())
    print ("\nClient authenticated")
    print("Connection accepted from " + repr(addr[1]))
    print("\n")

    #send the generated key and iv
    connstream.write("approved connection\n")
    connstream.write(encrypted_aes_key)
    connstream.write(iv)


    try:
        interact(connstream,cipher)
        #send back to client some encrypted data
        print(" 'Encrypted Response...' sent\n")
        connstream.write(cipher.encrypt(pad("Encrypted Response...")))
    finally: 
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
        
print ("\nConnection Closed!")



    

  