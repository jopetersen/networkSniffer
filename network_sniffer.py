# sniffers capture network traffic and analyze each packet of information
# an advanced example would be wireshark
# written IN python FOR Linux

import socket
#  a socket is an internal endpoint for sending/receiving data in a network
#creating an INET, raw socket
    # an INET is any network that uses an IP
    # a raw socket allows transfer of information without transport layer formatting
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#receive a packet
while True:
    print s.recvfrom(65565)
