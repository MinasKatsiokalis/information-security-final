
"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
"""

from Crypto.Cipher import AES

class AES_file(object):
    
    #Encrypts a file with AES-128 and save it to another file
    def encrypt(self,file_name_in, file_name_out, key, iv):
        #the file that plain text is in
        in_file = open(file_name_in, 'rb') 
        #the file the output saved     
        out_file = open(file_name_out, 'wb')
            
        bs = AES.block_size
        cipher = AES.new(key, AES.MODE_CBC, iv)
        finished = False
        while not finished:
            #read the file by 1024 blocks per visit
            chunk = in_file.read(1024 * bs)
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = bs - (len(chunk) % bs)
                chunk += padding_length * chr(padding_length)
                finished = True
            out_file.write(cipher.encrypt(chunk))
            
        in_file.close()
        out_file.close()
            
    #Decrypts a file with AES-128 and save it to another file
    def decrypt(self,file_name_in, file_name_out, key, iv):
        #the file that cipher text is in
        in_file = open(file_name_in, 'rb')  
        #the file the output saved    
        out_file = open(file_name_out, 'wb')
        
        bs = AES.block_size
        cipher = AES.new(key, AES.MODE_CBC, iv)
        next_chunk = ''
        finished = False
        while not finished:
            chunk= next_chunk
            #read the file by 1024 blocks per visit
            next_chunk = cipher.decrypt(in_file.read(1024 * bs))
            if len(next_chunk) == 0:
                padding_length = ord(chunk[-1])
                if padding_length < 1 or padding_length > bs:
                   raise ValueError("bad decrypt pad (%d)" % padding_length)
                # all the pad-bytes must be the same
                if chunk[-padding_length:] != (padding_length * chr(padding_length)):
                   raise ValueError("bad decrypt")
                chunk = chunk[:-padding_length]
                finished = True
            out_file.write(chunk)
            
        in_file.close()
        out_file.close()
        