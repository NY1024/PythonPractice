import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print '\n[*]'+str(hostname)+'FTP Anonymous Logon Succeeded'
        ftp.quit()
        return True
    except Exception,e:
        print '\n[-]'+str(hostname)+'FTP Anonymous Logon Faieed'
        return False
    host = '192.168.98.179'
    anonLogin(host)