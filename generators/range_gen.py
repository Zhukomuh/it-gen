def my_range(*args):
    """standard range func"""
    start, stop, step = 1, None, 1
    if len(args) == 1:
        stop = args
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError('Invalid data')

    if not isinstance(start, int):
        raise TypeError('my_range() args must be int')
    if not isinstance(stop, int):
        raise TypeError('my_range() args must be int')
    if not isinstance(step, int):
        raise TypeError('my_range() args must be int')
    if not step:
        raise ValueError('Step arg must be > 0')
    if step < 0 and stop > start:
        return
    if step > 0 and stop < start:
        return
    while abs(start) < abs(stop):
        yield start
        start += step


