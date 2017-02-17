from scapy.all import *
interface = 'mon0'
probeReqs = []
def sniffProbe(p):
    if p.haslayer(DotllProbeReq).info
        if netName not in probeReqs:
            probeReqs.append(netName)
            print '[+] Detected New Probe Request:'+netName
sniff(ifae=interface,prn=sniffProbe)