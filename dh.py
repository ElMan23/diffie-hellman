import converter


def diffie_hellman_server(b, s):

    p = converter.convert_bytes_to_int(s.recv(1024))
    s.send(b'Received p')
    g = converter.convert_bytes_to_int(s.recv(1024))
    s.send(b'Received g')
    B = (g ** b) % p
    A = converter.convert_bytes_to_int(s.recv(1024))
    s.send(converter.convert_int_to_bytes(B))
    K = (A ** b) % p

    return K


def diffie_hellman_client(p, g, a, s):

    s.send(converter.convert_int_to_bytes(p))
    # print(s.recv(1024))
    s.recv(1024)
    s.send(converter.convert_int_to_bytes(g))
    # print(s.recv(1024))
    s.recv(1024)
    A = (g ** a) % p
    s.send(converter.convert_int_to_bytes(A))
    B = converter.convert_bytes_to_int(s.recv(1024))
    K = (B ** a) % p

    return K