import yara
import os.path

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red

for root, dirs, files in os.walk('./'):
	
	for filename in files:
		
		print "\n[+] File Name : " + filename

		rules = yara.compile(filepath = "snslocker.yar")
		match = rules.match(filename)

		try:
			
			line = str(match[0])

			print(R+"[-] This file is Malware!"+W)

		except:

			print "[-] This file is not malware!"
