#include <pcap.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ether.h>
#include <arpa/inet.h>

#define SNAP_LEN 1518 // 패킷 캡처 최대 바이트 수 정의 //
#define SIZE_ETHERNET 14 // 이더넷 헤더 14 바이트 정의 //
#define ETHER_ADDR_LEN	6 // 이더넷 주소 6 바이트 정의 //

// 이더넷 헤더 구조체 //
struct sniff_ethernet {
        u_char  ether_dhost[ETHER_ADDR_LEN];    
        u_char  ether_shost[ETHER_ADDR_LEN];    
        u_short ether_type;                     
};

// IP 헤더 구조체 //
struct sniff_ip {
        u_char  ip_vhl;                 
        u_char  ip_tos;                 
        u_short ip_len;                 
        u_short ip_id;                  
        u_short ip_off;                 
        #define IP_RF 0x8000            
        #define IP_DF 0x4000            
        #define IP_MF 0x2000            
        #define IP_OFFMASK 0x1fff       
        u_char  ip_ttl;                 
        u_char  ip_p;                   
        u_short ip_sum;                 
        struct  in_addr ip_src,ip_dst;
};

// TCP 헤더 부분 //
typedef u_int tcp_seq;

struct sniff_tcp {
        u_short th_sport;              
        u_short th_dport;               
        tcp_seq th_seq;                 
        tcp_seq th_ack;                 
        u_char  th_offx2;               
	#define TH_OFF(th)      (((th)->th_offx2 & 0xf0) >> 4)
        u_char  th_flags;
        #define TH_FIN  0x01
        #define TH_SYN  0x02
        #define TH_RST  0x04
        #define TH_PUSH 0x08
        #define TH_ACK  0x10
        #define TH_URG  0x20
        #define TH_ECE  0x40
        #define TH_CWR  0x80
        #define TH_FLAGS        (TH_FIN|TH_SYN|TH_RST|TH_ACK|TH_URG|TH_ECE|TH_CWR)
        u_short th_win;                 
        u_short th_sum;                 
        u_short th_urp;                
};

#define IP_HL(ip)               (((ip)->ip_vhl) & 0x0f)
#define IP_V(ip)                (((ip)->ip_vhl) >> 4)

void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet); // 패킷을 받아 들인 경우 함수 호출 //

int main(int argc, char **argv)
{
	char *dev = NULL; // 패킷 캡처 장치 이름 //
	char errbuf[PCAP_ERRBUF_SIZE]; // 장치 로드 에러 발생시 에러 메시지 저장 //

	pcap_t *handle;	// 패킷 캡처 장치 핸들러 //

	int num_packets = 10; // 캡처할 패킷의 수 //
	char filter_exp[] = "ip"; // pcap_compile 옵션 지정 - 필터링 용도 //

	struct bpf_program fp; // 필터링 규칙에 의한 구조체 //

	bpf_u_int32 mask; // 서브넷 마스크 //
	bpf_u_int32 net; // 네트워크 //

	dev = pcap_lookupdev(errbuf); // 사용 패킷 캡처 장치 이름 얻어 오기 //

	pcap_lookupnet(dev, &net, &mask, errbuf); // 얻어온 장치의 네트워크 및 마스크 정보 얻어오기 //

	printf("Device Name : %s\n", dev); // 캡처한 장치 이름 출력하기 //
	printf("Number of packets : %d\n", num_packets); // 패킷의 수 출력 //

	handle = pcap_open_live(dev, SNAP_LEN, 1, 1000, errbuf);
	// 사용하는 장치의 핸들을 가져옴, (디바이스 지정, 받아들일 수 있는 패킷의 크기, PROMISCUOUS 모드 활성화, 읽기 시간 초과 지정, 에러 메시지 저장) //
	
	pcap_compile(handle, &fp, filter_exp, 0, net); // 패킷 필터링 용도, 필터 규칙은 TCPDUMP 참조 //

	pcap_setfilter(handle, &fp); // pcap_compile을 통해서 지정된 필터를 적용시키기 위해서 사용 //

	pcap_loop(handle, num_packets, got_packet, NULL); // 지정한 수만큼 패킷을 캡처해 해당 패킷을 got_packet에게 전달하고 함수 수행 //

	pcap_freecode(&fp); // PCAP 정리 //
	pcap_close(handle); // PCAP 핸들 종료 //

	return 0;
}

void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet) // 패킷을 받아 들인 경우 함수 호출 //
{
	static int count = 1; // 패킷 카운터 //
	
	const struct sniff_ethernet *ethernet; // Ethernet 헤더 //
	const struct sniff_ip *ip; // IP 헤더 //
	const struct sniff_tcp *tcp; // TCP 헤더 //

	int size_ip; // IP 패킷 사이즈 값 넣을 변수 선언 //
	
	printf("\nPacket number %d:\n", count); // 패킷 숫자 (증가) //
	count++;

	ethernet = (struct sniff_ethernet*)(packet); // 패킷의 시작 점을 받아옴 첫부분은 Ethernet //
	
	printf("Source MAC Address : %s\n", ether_ntoa(ethernet->ether_shost)); // Source MAC Address 출력 //
	printf("Destination MAC Address : %s\n", ether_ntoa(ethernet->ether_dhost)); // Destination MAC Address 출력 //

	ip = (struct sniff_ip*)(packet + SIZE_ETHERNET); // 패킷의 첫 시작 지점 + Ethernet 크기 = IP 시작점 //
	
	size_ip = IP_HL(ip)*4; // IP 패킷 사이즈 구하기 //
	
	printf("Source IP Address : %s\n", inet_ntoa(ip->ip_src)); // Source IP Address 출력 //
	printf("Destination IP Address : %s\n", inet_ntoa(ip->ip_dst)); // Destination IP Address 출력 //
	
	// 프로토콜 분류 출력 //	
	switch(ip->ip_p) {
		case IPPROTO_TCP:
			printf("Protocol: TCP\n"); // TCP 프로토콜 출력 //
			break;
		case IPPROTO_UDP:
			printf("Protocol: UDP\n"); // UDP 프로토콜 출력 //
			return;
		case IPPROTO_ICMP:
			printf("Protocol: ICMP\n"); // ICMP 프로토콜 출력 //
			return;
		case IPPROTO_IP:
			printf("Protocol: IP\n"); // IP 프로토콜 출력 //
			return;
		default:
			printf("Protocol: unknown\n"); // 알 수 없는 경우 출력 //
			return;
	}
	
	tcp = (struct sniff_tcp*)(packet + SIZE_ETHERNET + size_ip); // 패킷의 첫 시작 지점 + Ethernet 크기 + IP 크기 = TCP 시작점 //
	
	printf("Source Port: %d\n", ntohs(tcp->th_sport)); // Source Port 출력 //
	printf("Destination Port: %d\n", ntohs(tcp->th_dport)); // Destination Port 출력 //
	
	return;
}
