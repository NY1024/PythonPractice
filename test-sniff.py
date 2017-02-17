from scapy.all import *
def pktPrint(pkt):
    if pkt.haslayer(DotllBeacon):
        print '[+] Detected 802.11 Beacon Frame'
    elif pkt.haslayer(DotllProbeReq):
        print '[+] Detected 802.11 Probe Request Frame'
    elif pkt.haslayer(TCP):
        print '[+] Fetected a TCP Packet'
    elif pkt.haspayer(DNS):
        print '[+] Detected a DNS Pakcet'
conf.iface = 'mon0'
sniff(prn=pktPrint)