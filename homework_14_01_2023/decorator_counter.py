total_counter = {}


def deco_counter(func):
    """counting the quantity of func calls with save in global
    dict (total_counter) with key:func_name"""
    def inner(*args, **kwargs):

        global total_counter
        if func.__name__ in total_counter:
            total_counter[func.__name__] += 1
        else:
            total_counter[func.__name__] = 1

        return func(*args, **kwargs)
    return inner


@deco_counter
def add(x, y):
    return x + y


@deco_counter
def div(x, y):
    return x / y


if __name__ == '__main__':
    div(5, 4)
    div(6, 4)
    add(5, 4)
    add(6, 4)
    add(6, 4)
    add(6, 4)
    add(6, 4)
    print(total_counter)
