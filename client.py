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
if (len(sys.argv) < 3):
    print('Usage: python client.py <START_RANGE> <END_RANGE>')
    sys.exit(1)

start_range = int(sys.argv[1])
end_range = int(sys.argv[2])

if start_range >= end_range:
    print('Start range should be strictly less than end range')
    sys.exit(1)


p = prime.random_prime(start_range, end_range)
g = random.randint(start_range, end_range)
a = random.randint(start_range, end_range)


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