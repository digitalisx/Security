def MBRPt1():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] First Partition Information")
	
	bf1 = data[446:447].encode("hex")

	if bf1 == "80":

		print("[-] Boot Flag : 0x" + bf1 + " - Boot Enable")
	
	else:

		print("[-] Boot Flag : 0x" + bf1 + " - Boot Disable")

	sch1 = data[447:448].encode("hex")
	sch2 = data[448:449].encode("hex")
	sch3 = data[449:450].encode("hex")

	print("[-] Starting CHS Address : 0x" + sch3 + sch2 + sch1)

	pt1 = data[450:451].encode("hex")

	print("[-] Partition Type : 0x" + pt1)

	ech1 = data[451:452].encode("hex")
	ech2 = data[452:453].encode("hex")
	ech3 = data[453:454].encode("hex")
	
	print("[-] Ending CHS Address : 0x" + ech3 + ech2 + ech1)

	sla1 = data[454:455].encode("hex")
	sla2 = data[455:456].encode("hex")
	sla3 = data[456:457].encode("hex")
	sla4 = data[457:458].encode("hex")

	print("[-] Starting LBA Address : 0x" + sla4 + sla3 + sla2 + sla1)

	sz1 = data[458:459].encode("hex")
	sz2 = data[459:460].encode("hex")
	sz3 = data[460:461].encode("hex")
	sz4 = data[461:462].encode("hex")

	print("[-] Size of Sector : 0x" + sz4 + sz3 + sz2 + sz1)

MBRPt1()