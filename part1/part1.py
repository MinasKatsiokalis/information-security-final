"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
"""

import aes as Aes
import sha as Sha
import sign as Rsa
import cert_verification as cv

aes_128 = Aes.AES_file()
iv = '\xb2\x38\x33\x1a\xfe\xff\x07\x6c\xce\x7a\x5c\x30\xba\x30\xe0\x00'
sha_256 = Sha.SHA_file()
Sign = Rsa.Sign_file()
Cert = cv.Certificate()

#MENU
inpt = '0'
while (inpt <= '6') and (inpt >= '0'):
	print("\nInsert an option:")
	print("==========================")
	print("1.Encrypt file")
	print("2.Decrypt file")
	print("3.Hash File")
	print("4.Sign File")
	print("5.Signature Verification")
	print("6.Certificate Verification")
	print("0.Exit")
	print("==========================")
	inpt = raw_input("Type #-of-option and press enter:")

	if inpt == '1':
		plain_file = raw_input("Name of the file:")
		key = raw_input("Key (16 bytes):") 

		aes_128.encrypt(plain_file,'out.txt', key, iv)
		print('\nDone! Check file out.txt')

	elif inpt == '2':
		cipher_file = raw_input("Name of the file:")
		key = raw_input("Key (16 bytes):")
		    
		aes_128.decrypt(cipher_file,'out2.txt', key, iv)
		print('\nDone! Check file out2.txt')

	elif inpt == '3':
		plain_file = raw_input("Name of the file:")

		sha_256.hash(plain_file, 'out3.txt')
		print('\nDone! Check file out3.txt')

	elif inpt == '4':
		plain_file = raw_input("Name of the file to be signed:")
		pkey_file  = raw_input("Name of the private key file:")

		Sign.signature(pkey_file, plain_file)
		print('\nDone! Check file out4_sign.txt')

	elif inpt == '5':
		file_name_signed = raw_input("Name of the file was signed:")
		public_key  	 = raw_input("Name of the public key file:")
		sign_file     	 = raw_input("Name of the sign file:")

		Sign.validate(public_key, file_name_signed, sign_file)

	elif inpt == '6':
		file_name_in = raw_input("Name of the certificate file:")
		public_key_name  = raw_input("Name of the public key owner:")

		Cert.verify(public_key_name, file_name_in)

	elif inpt == '0':
		print("\nExit!")
		break

	else:
		print("\nWrong Input!")



  