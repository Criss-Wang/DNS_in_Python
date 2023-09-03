from .dns import build_response
from .setup import logger, sock


def main():
    while True:
        data, addr = sock.recvfrom(512)
        logger.info(f"data: {data}, addr: {addr}")
        response = build_response(data)
        sock.sendto(response, addr)
