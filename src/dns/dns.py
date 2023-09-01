from typing import Union, Tuple, TypeAlias, List, Dict, Any
# from typing_extensions import TypeAlias

from .zones import get_zone

byte: TypeAlias = Union[bytes, bytearray]

def get_flags(flags: byte) -> byte:
    byte1 = bytes(flags[0])
    print(flags, flags[0], byte1)
    byte2 = bytes(flags[1])

    rflags = ''

    QR = '1'

    OPCODE = ''

    for bit in range(1, 5):
        OPCODE += str(ord(byte1) & (1 << bit))

    AA, TC, RD, RA, Z, RCODE = '1', '0', '0', '0', '000', '0000'
    
    return int(QR + OPCODE + AA + TC + RD, 2).to_bytes(1, byteorder='big') + \
        int(RA + Z + RCODE, 2).to_bytes(1, byteorder='big')

def get_question_domain(data: byte) -> Tuple[List[Dict[str, Any]], str, List[str]]:
    state = 0
    domain_string = ''
    domain_parts = []
    current_string_size = 0
    current_position = 0
    for bytecode in data:
        if state == 1:
            if bytecode != 0:
                domain_string += chr(bytecode)
            current_string_size += 1

            if current_string_size == expected_length:
                domain_parts.append(domain_string)
                domain_string = ''
                state = 0
                current_string_size = 0
            if bytecode == 0:
                domain_parts.append(domain_string)
                break
        else:
            state = 1
            expected_length = bytecode
        current_position += 1

    question_type = data[current_position :current_position + 2]
    
    return (domain_parts, question_type)

def get_recs(data: byte) -> Tuple:
    domain_parts, question_type = get_question_domain(data)

    if question_type == b'\x00\x01':
        qt = 'a' # answer key
    zone = get_zone(domain_parts)
    
    return (zone[qt], qt, domain_parts)

def build_question(domain_name: List[str], rectype: str) -> byte:
    qbytes = b''

    for part in domain_name:
        length = len(part)
        qbytes += bytes([length])

        for char in part:
            qbytes += ord(char).to_bytes(1, byteorder='big')

    if rectype == 'a':
        qbytes += (1).to_bytes(2, byteorder='big') # type
    qbytes += (1).to_bytes(2, byteorder='big') # class
    return qbytes

def rec_to_bytes(rectype: str, recttl: int, recval: str) -> byte:
    rbytes = b"\xc0\x0c"

    if rectype == 'a':
        rbytes += bytes([0]) + bytes([1])

    rbytes += bytes([0]) + bytes([1])
    rbytes += int(recttl).to_bytes(4, byteorder='big')

    if rectype == 'a':
        rbytes += bytes([0]) + bytes([4])

    for part in recval.split("."):
        rbytes += bytes([int(part)])
    return rbytes

def build_response(data: byte) -> byte:
    """
    Refer to RFC 1035 Section 4.1.1 for Header format and details:
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                      ID                       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA|   Z    |   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    QDCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ANCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    NSCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                    ARCOUNT                    |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    """
    transaction_ID = data[:2] # first 2 bytes
    TID = ''
    for byte in transaction_ID:
        TID += hex(byte)[2:]

    # Get the flags (3rd and 4th bytes)
    flags = get_flags(data[2:4])    

    # Question count - default 1
    QDCOUNT = b'\x00\x01'

    # Answer count
    records, rectype, domain_name = get_recs(data[12:])
    ANCOUNT = len(records).to_bytes(2, byteorder='big')
    
    # Nameserver count
    NSCOUNT = (0).to_bytes(2, byteorder='big')

    # Additional Count
    ARCOUNT = (0).to_bytes(2, byteorder='big')

    dns_header = transaction_ID + flags + QDCOUNT + ANCOUNT + NSCOUNT + ARCOUNT

    dns_body = b''

    dns_question = build_question(domain_name, rectype)

    for record in records:
        dns_body += rec_to_bytes(rectype, record['ttl'], record['value'])
    return dns_header + dns_question + dns_body


