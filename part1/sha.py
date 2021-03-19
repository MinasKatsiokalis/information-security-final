"""
----------------------------------  
Minas Katsiokalis
AM: 2011030054 
email: minaskatsiokalis@gmail.com           
----------------------------------
"""

import hashlib

class SHA_file(object):

	def hash(self, file_name_in, file_name_out):
		#the file that plain text is in
		in_file = open(file_name_in, 'rb') 
		#the file the output saved     
		out_file = open(file_name_out, 'wb')

		# read stuff in 64kb chunks
		BUF_SIZE = 65536  
		sha_256 = hashlib.sha256()

		finished = False
		while not finished:
			data = in_file.read(BUF_SIZE)
			if len(data) == 0:
				finished = True
			sha_256.update(data)
		out_file.write(sha_256.hexdigest())

		in_file.close()
		out_file.close()
