# packet sniffer in python2 for linux
# sniffs the TCP packet

import socket, sys
from struct import *

#create an INET, streaming socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except socket.error, msg:
    print "Socket could not be created. Error code: " + str(msg[0]) + " Message"
    + msg[1]
    sys.exit()

#receive a packet
while True:
    packet = s.recvfrom (65565)
    #packet string from tuple
    packet = packet[0]


    #take first 20 characters for the ip header
    packet = packet[0:20]

    #unpacking them

    iph = unpack('BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >>4
    ihl = version_ihl & 0xF

    iph_length = ihl * 4
