import os
import sys
import hashlib
import time

def MBRUI():
	print"""
  __  __ ____  ____       _                _                    
 |  \/  | __ )|  _ \     / \   _ __   __ _| |_   _ _______ _ __ 
 | |\/| |  _ \| |_) |   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
 | |  | | |_) |  _ <   / ___ \| | | | (_| | | |_| |/ /  __/ |   
 |_|  |_|____/|_| \_\ /_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                             |___/             
	
	If you don`t know command, Please typing 'help'
	"""

def MBRTime():

	print("[+] MBR Analysis Time : " + time.ctime() + "\n") 

def MBRhash():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] Dump File Encrypt")
	print("[-] MBR Dump MD5 : " + hashlib.md5(data).hexdigest())
	print("[-] MBR Dump SHA1 : " + hashlib.sha1(data).hexdigest() + "\n")

	mbr.close()

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

def MBRBoot():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] MBR ETC Information")
	print("[-] MBR Device Signature : 0x" + data[440:444].encode("hex"))
	print("[-] MBR Error Message Offset : 0x" + data[437:440].encode("hex") + "\n")

	mbr.close()

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

def MBRPt2():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] Second Partition Information")
	
	bf2 = data[462:463].encode("hex")

	if bf2 == "80":

		print("[-] Boot Flag : 0x" + bf2 + " - Boot Enable")
	
	else:

		print("[-] Boot Flag : 0x" + bf2 + " - Boot Disable")

	sch1 = data[463:464].encode("hex")
	sch2 = data[464:465].encode("hex")
	sch3 = data[465:466].encode("hex")

	print("[-] Starting CHS Address : 0x" + sch3 + sch2 + sch1)

	pt1 = data[466:467].encode("hex")

	print("[-] Partition Type : 0x" + pt1)

	ech1 = data[467:468].encode("hex")
	ech2 = data[468:469].encode("hex")
	ech3 = data[469:470].encode("hex")
	
	print("[-] Ending CHS Address : 0x" + ech3 + ech2 + ech1)

	sla1 = data[470:471].encode("hex")
	sla2 = data[471:472].encode("hex")
	sla3 = data[472:473].encode("hex")
	sla4 = data[473:474].encode("hex")

	print("[-] Starting LBA Address : 0x" + sla4 + sla3 + sla2 + sla1)

	sz1 = data[474:475].encode("hex")
	sz2 = data[475:476].encode("hex")
	sz3 = data[476:477].encode("hex")
	sz4 = data[477:478].encode("hex")

	print("[-] Size of Sector : 0x" + sz4 + sz3 + sz2 + sz1)

def MBRPt3():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] Third Partition Information")
	
	bf3 = data[478:479].encode("hex")

	if bf3 == "80":

		print("[-] Boot Flag : 0x" + bf3 + " - Boot Enable")
	
	else:

		print("[-] Boot Flag : 0x" + bf3 + " - Boot Disable")

	sch1 = data[479:480].encode("hex")
	sch2 = data[480:481].encode("hex")
	sch3 = data[481:482].encode("hex")

	print("[-] Starting CHS Address : 0x" + sch3 + sch2 + sch1)

	pt1 = data[482:483].encode("hex")

	print("[-] Partition Type : 0x" + pt1)

	ech1 = data[483:484].encode("hex")
	ech2 = data[484:485].encode("hex")
	ech3 = data[485:486].encode("hex")
	
	print("[-] Ending CHS Address : 0x" + ech3 + ech2 + ech1)

	sla1 = data[486:487].encode("hex")
	sla2 = data[487:488].encode("hex")
	sla3 = data[488:489].encode("hex")
	sla4 = data[489:490].encode("hex")

	print("[-] Starting LBA Address : 0x" + sla4 + sla3 + sla2 + sla1)

	sz1 = data[490:491].encode("hex")
	sz2 = data[491:492].encode("hex")
	sz3 = data[492:493].encode("hex")
	sz4 = data[493:494].encode("hex")

	print("[-] Size of Sector : 0x" + sz4 + sz3 + sz2 + sz1)

def MBRPt4():

	mbr = open("mbr.bin", 'rb')
	data = mbr.read()

	print("\n[+] Fourth Partition Information")
	
	bf4 = data[494:495].encode("hex")

	if bf4 == "80":

		print("[-] Boot Flag : 0x" + bf4 + " - Boot Enable")
	
	else:

		print("[-] Boot Flag : 0x" + bf4 + " - Boot Disable")

	sch1 = data[495:496].encode("hex")
	sch2 = data[496:497].encode("hex")
	sch3 = data[497:498].encode("hex")

	print("[-] Starting CHS Address : 0x" + sch3 + sch2 + sch1)

	pt1 = data[498:499].encode("hex")

	print("[-] Partition Type : 0x" + pt1)

	ech1 = data[499:500].encode("hex")
	ech2 = data[500:501].encode("hex")
	ech3 = data[501:502].encode("hex")
	
	print("[-] Ending CHS Address : 0x" + ech3 + ech2 + ech1)

	sla1 = data[502:503].encode("hex")
	sla2 = data[503:504].encode("hex")
	sla3 = data[504:505].encode("hex")
	sla4 = data[505:506].encode("hex")

	print("[-] Starting LBA Address : 0x" + sla4 + sla3 + sla2 + sla1)

	sz1 = data[506:507].encode("hex")
	sz2 = data[507:508].encode("hex")
	sz3 = data[508:509].encode("hex")
	sz4 = data[509:510].encode("hex")

	print("[-] Size of Sector : 0x" + sz4 + sz3 + sz2 + sz1 + "\n")

def com():
	if command == "time":
		MBRTime()
	
	elif command == "hash":
		MBRhash()

	elif command == "sig":
		MBRSig()

	elif command == "etc":
		MBRBoot()

	elif command == "pti":
		MBRPt1()
		MBRPt2()
		MBRPt3()
		MBRPt4()

	elif command == "help":
		print """
		MBR Analysis Command help
		(Support Only Small Character)

		View Time : time
		View MBR Dump file Hash : hash
		View MBR Signature & Check : sig
		View MBR GUID, Error Message Offset : etc
		View MBR Partition Table Entry : pti
		Clear Command Line : cls
		Program Exit : exit

		Developed By Digitalisx
		"""

	elif command == "cls":
		os.system("cls")
		MBRUI()

	elif command == "exit":
		exit()

	elif(len(command) == 0):
		pass

	else:
		print "\n                   Command is Not Found!\n"

MBRUI()

while(1):
	command = raw_input("                   Typing Command : ")
	com()