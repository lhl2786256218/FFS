def fuzzing1_e ():
    import socket
    FUZZ = ""
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        while True:
            FUZZ += "A" * 10
            print("Fuzzing with {} bytes".format(len(FUZZ)))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = s.connect((host, 21))
            s.recv(1024)
            s.send(b"USER " + FUZZ.encode() + b"\r\n")
            s.close()
    else:
        print ("Error!")
def fuzzing1_c ():
    import socket
    FUZZ = ""
    print ("请输入目标主机IP!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        while True:
            FUZZ += "A" * 10
            print("Fuzzing with {} bytes".format(len(FUZZ)))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect = s.connect((host, 21))
            s.recv(1024)
            s.send(b"USER " + FUZZ.encode() + b"\r\n")
            s.close()
    else:
        print("错误!")