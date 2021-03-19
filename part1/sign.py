"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
"""

from Crypto.PublicKey import RSA 
from Crypto.Hash import SHA256

class Sign_file(object):
    def signature(self, private_key, file_name_in):  
        pkey = open(private_key, 'rb').read() 
        data = open(file_name_in, 'rb').read() 

        #hashing the data
        hash_data = SHA256.new(data).hexdigest()
        key = RSA.importKey(pkey)

        #signature created using private key
        signature = key.decrypt(hash_data)

        #the file the output saved     
        out_file = open('out4_sign.txt', 'wb')
        out_file.write(signature)
        out_file.close()

    def validate(self, public_key, file_name_signed, sign_file):
        data = open(file_name_signed, 'rb').read() 
        signature = open(sign_file, 'rb').read()
        pub_key = open(public_key, "rb").read()
        
        hash_data = SHA256.new(data).hexdigest()
        key = RSA.importKey(pub_key)

        #signature verified using public key
        valid = key.encrypt(signature,32)
        
        if valid[0] == hash_data:
            print ("\nSignature Verified!")
            return True
        else:
            print ("\nSignature Not Verified!")
            return False