def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))
