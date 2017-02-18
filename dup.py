from scapy.all import *
def dupRadio(pkt):
    rPkt=pkt.getlayer(RadioTap)
    version=rPkt.version
    pad=rPkt.pad
    present=rPkt.present
    notedecoded=rPkt.notedecoded
    nPkt = RadioTap(version,pad=pad,present=present,notedecoded)
    return nPkt
def dupDotll(pkt):
    dPkt=pkt.getlayer(Dotll)
    subtype=dPkt.subtype
    Type=dPkt.type
    proto=dPkt.proto
    FCfield=dPkt.FCfield
    ID=dPkt.ID
    addr1=dPkt.addr1
    addr2=dPkt.addr2
    addr3=dPkt.addr3
    SC=dPkt.SC
    addr4=dPkt.addr4
    nPkt=Dotll(subtype=subtype,type=Type,proto=proto,FCfield=FCfield,ID=ID,addr1=addr1,addr2,addr2,addr3=addr3,addr4=addr4)
    return nPkt
def dupSNAP(pkt):
    sPkt=pkt.getlayer(SNAP)
    oui=sPkt.OUI
    code=sPkt.code
    nPkt=SNAP(OUT=oui,code=code)
    return nPkt
def dupLLC(pkt):
    1Pkt=pkt.getlayer(LLC)
    dsap=1Pkt.dsap
    ssap=1Pkt.ssap
    ctrl=1Pkt.ctrl
    nPkt=LLC(dsap=dsap,ssap=ssap,ctrl=ctrl)
    return nPkt
def dupIP(pkt):
    iPkt=pkt.getlayer(IP)
    version=iPkt.version
    tos=iPkt.tos
    ID=iPkt.id
    flags=iPkt.flags
    ttl=iPkt.ttl
    proto=iPkt.proto
    src=iPkt.src
    dst=iPkt.dst
    options=iPkt.options
    nPkt=IP(version=version,id=ID,tos=tos,flags=flags,ttl=ttl,proto=proto,src=src,dst=dst,options=options)
    return nPkt
def dupUDP(pkt):
    uPkt=pkt.getlayer(UDP)
    sport=uPkt.sport
    dport=uPkt.dport
    npKt=UDP(sport=sport,dport=dport)
    return nPkt