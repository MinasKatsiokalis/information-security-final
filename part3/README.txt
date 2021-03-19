----------| PART 3 |-------------
-In order to execute properly, 2 instances (2 consoles) of Spyder (or any other software) need to be executed.
-On first instance, run server_app.py
-On second instance run client_app.py 
-The server_app.py file has to be executed first

A simple implementation 
A connection between the server and the client takes place
Both ways authentication.
Server ganarates an AES_128 key encrypts it with client's public_key and send it to client
Client recieves the encrypted key, decrypts it with his private_key 
Client send some encrypted(AES-128) data via keyboard, server recieve them and print them.
Server send encrypted response (AES-128), client recieve it and print it.
Connection is terminated.

-Certificates and keys generated and signed with OpenSSL, with RSA 2048.