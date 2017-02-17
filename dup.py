from scapy.all import *
def dupRadio(pkt):
    rPkt=pkt.getlayer(RadioTap)
    version=rPkt.version
    pad=rPkt.pad
    present=rpkt.present
    notdecoded=rPktnotdecoded
    nPkt=RadioTap(version=version,pad=pad,present=present,notdecoded=notdecoded)
    return nPkt
def dupDotll(pkt):
    dPkt=pkt.getlayer(Dotll)
    subtype=dPkt.subtype
    Type=dPkt.type
    proto=dPkt.proto
    FCfield=dPkt.FCfield
    ID=dPkt.addr1
    addr1=dPkt.addr1
    addr2=dPkt.addr2
    addr3=dpkt.addr3
    SC=dPkt.SC
    addr4=addr4
    nPkt=Dotll(subtype=sutype,type=Type,proto=proto,FCfield=FCfield,ID=ID,addr1=addr1,addr2=addr2,addr3=addr3,SC=SC,addr4=addr4)
    return nPkt
def dup