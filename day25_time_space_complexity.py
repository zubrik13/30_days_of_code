def is_prime(n):
    """
    Highly inefficient!!!
    Method to determine whether an input number is Prime
    :param n: input integer
    :return: prints "Prime" in case a num is prime, and "Not prime" otherwise
    """
    if n <= 1:
        return False
    elif (n % 2 == 0) or (type(n**0.5) is not float):
        return False

    for num in range(3, n//2, 2):
        if n % num == 0:
            return False
    else:
        return True


def is_prime_opt(n):
    """
    Method to determine whether an input number is Prime
    :param n: input integer
    :return: prints "Prime" in case a num is prime, and "Not prime" otherwise
    """
    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


primes = dict()
primes[2] = None
primes[3] = None
primes[5] = None
primes[7] = None
primes[11] = None
# print(primes.keys())
# T = int(input())
T = 3
lst = [12, 5, 7]
for item in lst:
    if item in primes.keys():
        print("Prime")
    else:
        if is_prime_opt(item):
            primes[item] = None
            print("Prime")
        else:
            print("Not prime")