import socket
import converter


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diffie-Hellman parameters
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
p = 59  # Prime
g = 15  # Generator
a = 17  # Secret


def main():
    s = socket.socket()

    host = '127.0.0.1'
    port = 8081

    s.connect((host, port))

    # print(s.recv(1024))
    # print(converter.convert_bytes_to_int(s.recv(1024)))
    # s.send(b'Ciao')

    diffie_hellman_client(p, g, a, s)

    s.close()


def diffie_hellman_client(p, g, a, s):

    s.send(converter.convert_int_to_bytes(p))
    print(s.recv(1024))
    s.send(converter.convert_int_to_bytes(g))
    print(s.recv(1024))
    A = (g ** a) % p
    s.send(converter.convert_int_to_bytes(A))
    B = converter.convert_bytes_to_int(s.recv(1024))
    K = (B ** a) % p

    print('Shared secret:', K)


if __name__ == '__main__':
    main()