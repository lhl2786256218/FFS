def fuzzing3_e():
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    print ("Please enter fuzz characters!")
    FUZZin = input()
    FUZZ = str(FUZZin)
    if len(FUZZ) > 0 and len(host) > 0: 
        import socket
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host,21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + b"\r\n")
        s.close()
    else:
        print("Error!")
def fuzzing3_c():
    print ("请输入目标主机IP！")
    hostin = input()
    host = str(hostin)
    print ("请输入随机的模糊测试字符！")
    FUZZin = input()
    FUZZ = str(FUZZin)
    if len(FUZZ) > 0 and len(host) > 0: 
        import socket
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host,21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + b"\r\n")
        s.close()
    else:
        print("错误!")