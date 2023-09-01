import socket

from .dns import build_response

port = 10053 # DNS port to listen to
ip = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPv4, UDP
sock.bind((ip, port))

def main():
    while True:
        data, addr = sock.recvfrom(512)
        response = build_response(data)
        sock.sendto(response,addr)