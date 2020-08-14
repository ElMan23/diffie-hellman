import random

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                # print(n, "is not a prime number")
                # print(i, "times", n // i, "is", n)
                return False
                break
            else:
                # print(n, "is a prime number")
                return True
        else:
            # print(n, "is not a prime number")
            return False


def random_prime(range):
    n = random.randint(1, range)
    while not is_prime(n):
        n = random.randint(0, range)
    return n