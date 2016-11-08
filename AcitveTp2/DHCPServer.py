from scapy.all import *
from sys import *
import uuid


def get_mac():
    mac_num = hex(uuid.getnode()).replace('x', '').upper()
    mac = ':'.join(mac_num[i:i+2] for i in range(0,11,2))
    return str(mac)

server_mac = get_mac()
sn_mask = "255.255.255.0"
broadcast_mac = "FF:FF:FF:FF:FF:FF"
broadcast_ip = "255.255.255.255"
IPPrefix = "172.16.1."
IPSuffix = 99
IPToGive = "192.168.1.92"
renewalTime = 1800
leaseTime = 3150

def generateIP():
    global IPSuffix
    IPSuffix += 1
    return IPPrefix +str(IPSuffix)


def DHCPMonitorCallBack(pkt):
    if DHCP in pkt :

        if pkt[DHCP].options[0][1] == 1:
            print("DHCP Discover Packet Found")
            print(pkt[DHCP].options[2][1])
            DHCP_Offer(pkt)
        if pkt[DHCP].options[0][1] == 3:
            print("DHCP Request Packet Found")
            print(pkt[DHCP].options[2][1])
            DHCP_ACK(pkt)




def DHCP_Offer(pkt):
    global IPToGive
    global discoverRequestReceived
    response =  Ether(src=server_mac,
                      dst = broadcast_mac)/\
                IP(src = server_ip,
                   dst = broadcast_ip,
                   flags = "DF")/\
                UDP(sport=67,
                    dport=68)/\
                BOOTP( op=2,
                       yiaddr = IPToGive,
                       siaddr=server_ip,
                       giaddr=server_ip,
                       chaddr=pkt[BOOTP].chaddr ,
                       xid=pkt[BOOTP].xid,
                       flags = 0x0000)/ \
                DHCP(options=[('message-type', 'offer'),
                              ('subnet_mask', sn_mask),
                              ('router', server_ip),
                              ('name_server', server_ip),
                              ('server_id', server_ip),
                              ('renewal_time',renewalTime),
                              ('lease_time',leaseTime),
                              'end'])
    print("DHCP Offer IP: "+ IPToGive + "-> MAC: " + pkt[Ether].src)
    sendp(response)

def DHCP_ACK(pkt):
    global discoverRequestReceived
    response =  Ether(src=server_mac,
                      dst=broadcast_mac) / \
                IP(src=server_ip,
                   dst=broadcast_ip,
                   flags = "DF") / \
                UDP(sport=67,
                    dport=68) / \
                BOOTP(op=2,
                      yiaddr=IPToGive,
                      siaddr=server_ip,
                      giaddr=server_ip,
                      chaddr=pkt[BOOTP].chaddr,
                      xid=pkt[BOOTP].xid,
                      flags=0x0000) / \
                DHCP(options=[('message-type', 'ack'),
                              ('subnet_mask', sn_mask),
                              ('router', server_ip),
                              ('name_server', server_ip),
                              ('server_id', server_ip),
                              ('renewal_time',renewalTime),
                              ('lease_time',leaseTime),
                              'end'])
    print("DHCP ACK IP: "+ IPToGive + "-> MAC: " + pkt[Ether].src)
    sendp(response)


def DHCP_Decline(pkt):
    global discoverRequestReceived
    discoverRequestReceived = False
    response = Ether(src=server_mac,
                     dst=broadcast_mac) / \
               IP(src=server_ip,
                  dst=broadcast_ip,
                  flags="DF") / \
               UDP(sport=67,
                   dport=68) / \
               BOOTP(op=2,
                     yiaddr=IPToGive,
                     siaddr=server_ip,
                     giaddr=server_ip,
                     chaddr=pkt[BOOTP].chaddr,
                     xid=pkt[BOOTP].xid, flags=0x0000) / \
               DHCP(options=[('message-type', 'nak'), 'end'])
    print("DHCP DECLINE Sent")
    sendp(response)

if __name__ == "__main__":
    server_ip = sys.argv[1]
    sniff(prn=DHCPMonitorCallBack)
