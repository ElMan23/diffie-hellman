import sys
import socket
import random
import dh.dh as dh


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Diffie-Hellman parameters
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# b = 24  # Secret

# To take input from the user
# b = int(input("Enter the range: "))
# To use the arguments
if (len(sys.argv) < 3):
    print('Usage: python server.py <START_RANGE> <END_RANGE>')
    sys.exit(1)

start_range = int(sys.argv[1])
end_range = int(sys.argv[2])

if start_range >= end_range:
    print('Start range should be strictly less than end range')
    sys.exit(1)


b = random.randint(start_range, end_range)


def main():
    s = socket.socket()
    print("Socket successfully created")

    host = '127.0.0.1'
    port = 8081

    s.bind((host, port))
    print("Socket binded to port ", port)

    s.listen(5)
    print("Socket listening")

    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        # c.send(b'Thank you for connecting')
        # c.send(converter.convert_int_to_bytes(37))
        # print(c.recv(1024))

        K = 0
        while K == 0:
            K = dh.diffie_hellman_server(b, c)
        print('Shared secret:', K)

        c.close()


if __name__ == '__main__':
    main()