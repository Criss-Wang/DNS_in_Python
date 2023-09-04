import socket
import logging.config
import os

port = 10053  # DNS port to listen to
ip = "127.0.0.1"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # IPv4, UDP
sock.bind((ip, port))

os.chdir(os.path.dirname(__file__))

if not os.path.exists("logs"):
    os.mkdir("logs")
with open("logs/file.log", "w") as f:
    pass

logging.config.fileConfig('configs/logging_config.ini')
logger = logging.getLogger(__name__)
