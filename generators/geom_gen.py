def geometric_gen(start: int, stop: int, mul: int):
    """geometric progression generator with start, stop and multiple args"""
    while start < stop:
        yield start
        start *= mul


