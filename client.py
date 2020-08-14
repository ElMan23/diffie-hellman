import sys
import socket
import random
import dh
import prime


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diffie-Hellman parameters
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# p = 59  # Prime
# g = 37  # Generator
# a = 17  # Secret


# To take input from the user
# a = int(input("Enter the range: "))
# To use the arguments
if (len(sys.argv) < 2):
    print('Usage: python client.py <RANGE>')
range = int(sys.argv[1])
p = prime.random_prime(range)
g = random.randint(1, range)
a = random.randint(1, range)


def main():
    s = socket.socket()

    host = '127.0.0.1'
    port = 8081

    s.connect((host, port))

    # print(s.recv(1024))
    # print(converter.convert_bytes_to_int(s.recv(1024)))
    # s.send(b'Ciao')

    K = 0
    while K == 0:
        K = dh.diffie_hellman_client(p, g, a, s)
    print('Shared secret:', K)

    s.close()


if __name__ == '__main__':
    main()