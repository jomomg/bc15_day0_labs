def is_prime(n):
    """Checks whether a number n is a prime number"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """Generates a list of prime numbers between 0 and n"""
    if not isinstance(n, int):
        return "only integer input allowed"
    elif n <= 0:
        return "invalid input"
    elif n > 1000:
        return "input exceeds 1000"
    primes_list = []
    for i in range(2, n):
        if is_prime(i):
            primes_list.append(i)
    return primes_list


