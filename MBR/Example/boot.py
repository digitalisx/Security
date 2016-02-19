def MBRBoot():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("[+] MBR ETC Information")
	print("[-] MBR Device Signature : 0x" + data[440:444].encode("hex"))
	print("[-] MBR Error Message Offset : 0x" + data[437:440].encode("hex"))

	mbr.close()

MBRBoot()