def prime_gen(stop: int):
    """prime number generator"""
    for n in range(2, stop + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
