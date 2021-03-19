----------| PART 2 |-------------
-In order to execute properly, 2 instances(2 consoles) of Spyder (or any other software) need to be executed.
-On first instance, run server.py
-On second instance run client.py 
-The server.py file has to be executed first

A simple implementation 
A connection between the server and the client takes place
Client send some data via keyboard, server recieve them and print them
Connection is terminated.

-Files 'cert.pem' and 'key.pem' are the of the server for certificate and key 
in order to be authenticated by client (one-way-authentication)

-Certificate and keys generated and signed with OpenSSL, with RSA 2048.