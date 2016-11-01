import scapy.layers.l2
import scapy.route
import socket
    
interface = "enp0s3"
net = "192.168.1.0/24"

ans, unans = scapy.layers.l2.arping(net, iface=interface, timeout=1)
for s, r in ans.res:
    try:
        hostname = socket.gethostbyaddr(r.psrc)
    except socket.herror:
        pass

#Inspire de : https://github.com/bwaldvogel/neighbourhood


