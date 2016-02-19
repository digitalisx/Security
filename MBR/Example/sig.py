def MBRSig():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] MBR Signature Check")
	print("[-] MBR Signature : 0x" + data[511:512].encode("hex") + data[510:511].encode("hex"))

	sig = data[510:512].encode("hex")
	
	if sig == '55aa': 
		
		print("[-] Signature Safety Check : Safety\n")
	
	else:
		
		print("[-] Signature Safety Check : Warning\n")	

	mbr.close()

MBRSig()