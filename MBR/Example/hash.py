import hashlib

def MBRhash():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] Dump File Encrypt")
	print("[-] MBR Dump MD5 : " + hashlib.md5(data).hexdigest())
	print("[-] MBR Dump SHA1 : " + hashlib.sha1(data).hexdigest() + "\n")

	mbr.close()

MBRhash()