
from scapy.all import Ether,IP

# intialization of all the frames 80-91-33-C5-7D-ED
ether_frame = Ether()/IP()
ether_frame