#!/usr/bin/env python3

##
## EPITECH PROJECT, 2019
## test
## File description:
## [enter description here]
##

import socket
import sys

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888
    try:
        soc.connect((host, port))
    except:
        print("Error, connection failed")
        sys.exit()
    print("Enter 'quit' to exit")
    message = input("")
    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
            pass
        message = input("")
    soc.send(b'--quit--')

if __name__ == "__main__":
    main()
