"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
""" 

from OpenSSL import crypto as c

class Certificate(object):

    def verify(self, public_key_name, file_name_in):
    	#read the certificate
		cert = c.load_certificate(c.FILETYPE_PEM, file(file_name_in).read())
		components = cert.get_subject().get_components()
		#get subject name and date of expiration
		subject_name = components[5][1]
		expired = cert.has_expired()

		#check if the certifiacte has expired and
		#the name of the subject to be the same with public_key name
		if expired or (subject_name != public_key_name):
			print ("\nCertificate Not Verified!")
			return False
		else:
			print ("\nCertificate Verified!")
			return True

