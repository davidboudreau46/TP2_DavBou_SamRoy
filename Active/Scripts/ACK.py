from scapy.all import *
import sys

def response_SYN(pkt):
    if pkt.haslayer(TCP):
        sendsynack(pkt)

def sendsynack(pkt):
    ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
    SYN = TCP(sport=pkt[TCP].dport, dport=pkt[TCP].sport, flags='S', seq=1000)
    SYNACK = sr1(ip / SYN)

    response = IP(src=pkt[IP].dst,
                  dst=pkt[IP].src)/ \
               TCP(sport=pkt[TCP].dport,
                   dport=pkt[TCP].sport,
                   flags='A',
                   seq=SYNACK.ack + 1,
                   ack=SYNACK.seq + 1)
    send(response)

sniff(prn=response_SYN)