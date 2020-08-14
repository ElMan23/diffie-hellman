import socket
import dh


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diffie-Hellman parameters
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
p = 59  # Prime
g = 37  # Generator
a = 17  # Secret


def main():
    s = socket.socket()

    host = '127.0.0.1'
    port = 8081

    s.connect((host, port))

    # print(s.recv(1024))
    # print(converter.convert_bytes_to_int(s.recv(1024)))
    # s.send(b'Ciao')

    K = dh.diffie_hellman_client(p, g, a, s)
    print('Shared secret:', K)

    s.close()


if __name__ == '__main__':
    main()