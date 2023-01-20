def func(data):
    return data ** 2


def gen_func(start: int, quantity: int, user_func):
    index = 0
    while quantity > index:
        yield user_func(start)
        start += 1
        index += 1


if __name__ == '__main__':
    g = gen_func(1, 10, func)
    for i in g:
        print(i)
