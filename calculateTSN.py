from scapy.all import *
def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1,5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = srl(pkt,verbose=0)
        seqNum = ans.getlayer(TCP).seq
        dissSeq = seqNum - preNum
        print '[+] TCP Seq Difference:'+str(diffSeq)
    return seqNum + diffSeq
tgt = "192.168.1.106"
seqNum = calTSN(tgt)
print "[+] Next TCP Sequence Number to ACK is:"str(seqNum+1)
