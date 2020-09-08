def convert_bytes_to_int(b):
    # s = str(data, 'utf8')
    # n = int(s)
    n = int(str(b.decode('utf8')))
    return n


def convert_int_to_bytes(n):
    # b = bytes(str(data), 'utf8')
    b = (str(n)).encode('utf8')
    return b